# 카테고리 리스트 수집

import requests
import json
import datetime
import sys

w_date = datetime.datetime.now().strftime("%Y%m%d")

url = 'https://www.uniqlo.com/kr/ko/spa-cms/content/kr/ko/global/hamburger.json'
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'}

r = requests.get(url, headers=headers)

uniq1 = json.loads(r.text)
uniq2 = uniq1['tree']

cate_list = []
for i in uniq2:
    uniq3 = i['children']
    cate_1 = i['name']
    for i in uniq3:
        uniq4 = i['children']
        cate_2 = i['name']
        for i in uniq4:
            cate_3 = i['name']
            cate_id = i['id']
            if cate_id != "":
                cate_list.append([cate_1, cate_2, cate_3, cate_id])

cate_cnt = len(cate_list)

for cate_no, cateinfo in enumerate(cate_list[:]):
    cate_id = cateinfo[3]
    cate_1 = cateinfo[0]
    cate_1 = cate_1.replace('(mobile)', '')
    cate_2 = cateinfo[1]
    cate_3 = cateinfo[2]

    url = f'http://www.uniqlo.com/kr/ko/spa-catalog/products?category={cate_id}'
    r = requests.get(url, headers=headers)
    uniq4_1 = json.loads(r.text)

    page = (int(uniq4_1['total']) // 20) + 1

    for p in range(1, page + 1):
        p_url = url + f'&page={p}'
        r = requests.get(p_url, headers=headers)
        uniq5 = json.loads(r.text)
        if uniq5['total'] != 0:
            uniq6 = uniq5['records']
            for n, i6 in enumerate(uniq6):
                uniq7 = i6['SKUs']
                review_cnt = str(i6['reviewCount'])
                prd_id = i6['id']
                prd_nm_base = i6['name']
                base_price = i6['basePrice']
                prd_info = i6['productArtcInfo']
                color_list = i6['colors']
                img_url = ''
                rank = n + 1 + ((p - 1) * 20)
                img = i6['images']
                for k in img.keys():
                    img_url = img[k]

                size_table = i6['sizeLookupTablePath'] + i6['sizeLookupTable']

                prd_info = i6['productArtcInfo']
                material = ''
                manu_country = ''
                manu_month = ''
                for info in prd_info:
                    if info.get('key') == '001':
                        material = info.get('value').get('itemCont')
                        material = material.replace('\n', '')
                        material = material.replace('<br>', '')
                    elif info.get('key') == '005':
                        manu_country = info.get('value').get('itemCont')
                    elif info.get('key') == '007':
                        manu_month = info.get('value').get('itemCont')
                if manu_month != '':
                    manu_month = manu_month.replace('년', '')
                    manu_month = manu_month.replace('월', '')
                    manu_month = manu_month.replace('~', '')
                    manu_month = manu_month.replace(' ', '')
                    if len(manu_month) != 6:
                        manu_month = manu_month[:4] + '0' + manu_month[4:]

                prd_flag = i6['flags']
                event = ''
                for fl in prd_flag:
                    flag_name = fl['name']
                    flag_name.replace('\n', '').replace('"', '')
                    flag_description = fl['description'].replace('"', '')
                    if flag_description == '':
                        flag_description = 'no description'
                    event += '{"' + flag_name + '","' + flag_description.strip() + '"},'
                event = event[:-1]

                total_qty = 0
                price = ''
                dc_rate = ''
                for i7 in uniq7:
                    price = i7['salePrice']
                    dc_rate = (int(base_price) - int(price)) / int(base_price)
                    dc_rate = f'{dc_rate:0.2f}'
                    quantity = i7['investmentQuantity']
                    total_qty += quantity
                    skuID = i7['SKUUniqueID'][:10]
                    color = i7['color']
                    if i7['size_name']:
                        size = i7['size_name']
                    else:
                        size = ''

                    sku_dic = {}
                    sku_dic['w_date'] = w_date
                    sku_dic['prd_id'] = prd_id
                    sku_dic['color_id'] = color
                    sku_dic['size'] = size
                    sku_dic['quantity'] = quantity

                    with open(f'./result/uniqlo_sku_{w_date}.jl', 'a') as fsk:
                        fsk.write(json.dumps(sku_dic) + '\n')

                prd_url = f'https://store-kr.uniqlo.com/display/showDisplayCache.lecs?goodsNo={skuID}'

                selling_point = i6['htmlDetailDescription'].replace('\r\n', '').replace('\n', '')
                sp_dic = {}
                sp_dic['w_date'] = w_date
                sp_dic['prd_id'] = prd_id
                sp_dic['selling_point'] = selling_point
                with open(f'./result/uniqlo_sp_{w_date}.jl', 'a') as fsp:
                    fsp.write(json.dumps(sp_dic) + '\n')

                result_dic = {}
                result_dic['w_date'] = w_date
                result_dic['cate_1'] = cate_1
                result_dic['cate_2'] = cate_2
                result_dic['cate_3'] = cate_3
                result_dic['cate_id'] = cate_id
                result_dic['prd_id'] = prd_id
                result_dic['prd_nm'] = prd_nm_base.strip()
                result_dic['img_url'] = img_url

                result_dic['material'] = material
                result_dic['manu_country'] = manu_country
                result_dic['manu_month'] = manu_month
                result_dic['event'] = event
                result_dic['size_table'] = size_table

                result_dic['rank'] = str(rank)
                result_dic['price'] = str(price)
                result_dic['base_price'] = str(base_price)
                result_dic['dc_rate'] = dc_rate
                result_dic['stock'] = str(total_qty)
                result_dic['review_cnt'] = review_cnt
                result_dic['prd_url'] = prd_url

                with open(f'./result/uniqlo_{w_date}.jl', 'a') as f:
                    f.write(json.dumps(result_dic) + '\n')

        sys.stdout.write(f'\r{cate_id} - {cate_no + 1} / {cate_cnt} | {p} / {page}                ')
        sys.stdout.flush()
