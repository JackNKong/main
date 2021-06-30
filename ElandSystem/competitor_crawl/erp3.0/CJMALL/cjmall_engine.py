### 카테고리 수집

import requests
import json
from datetime import *
import time
import traceback


def get_prd(url):
    headers = {'Connection': 'Keep-Alive'}
    res = requests.get(url=url,headers=headers)
    js = json.loads(res.text)
    if res.status_code == 200:
        return js
    else:
        print(f'<<<<<<< URL not accessable >>>>>> {url}')
        return None


url = 'http://search.cjmall.com/search-web/search/cjmall/categoryItem.json?sc=G00011'

js = get_prd(url)

cate_list = list(
    [x['groupDatas']['CAT_INFO'] for x in js['result'] if x['type'] == "CJMALL_CATEGORY_ITEM_CATEGORY"][0].keys())

cate_dic = {}
for cate in cate_list:
    cate_split = cate.split('^')
    l_cate_nm = cate_split[0].split('_')[0]
    l_cate_cd = cate_split[0].split('_')[1]
    m_cate_nm = cate_split[1].split('_')[0]
    m_cate_cd = cate_split[1].split('_')[1]
    s_cate_nm = cate_split[2].split('_')[0]
    s_cate_cd = cate_split[2].split('_')[1]

    if l_cate_nm not in cate_dic:
        cate_dic[l_cate_nm] = {}
        cate_dic[l_cate_nm]['cd'] = l_cate_cd
        cate_dic[l_cate_nm]['children'] = {}

    if m_cate_nm not in cate_dic[l_cate_nm]['children']:
        m_cate_dic = {}
        m_cate_dic['cd'] = m_cate_cd
        m_cate_dic['children'] = {}
        cate_dic[l_cate_nm]['children'][m_cate_nm] = m_cate_dic

    if s_cate_nm not in cate_dic[l_cate_nm]['children'][m_cate_nm]['children']:
        s_cate_dic = {}
        s_cate_dic['cd'] = s_cate_cd
        cate_dic[l_cate_nm]['children'][m_cate_nm]['children'][s_cate_nm] = s_cate_dic

with open('./cate_dic_kr.json', 'w') as f:
    f.write(str(cate_dic))

with open('./cate_dic.json', 'w') as f:
    f.write(json.dumps(cate_dic))

### 상품 수집

import requests
import json
from datetime import *
import time
import traceback
import sys


def get_prd(url):
    res = requests.get(url=url)  # ,headers=headers)
    prd = json.loads(res.text)
    if res.status_code == 200:
        return prd
    else:
        print(f'<<<<<<< URL not accessable >>>>>> {url}')
        return None


def get_cate(cate_cd):
    #     url = 'http://search.cjmall.com/search-web/search/cjmall/categoryItem.json?t=API&o=BEST_SELLING_DESC&sc=%s&of=48&s=48&listingType=2&chn=30001001'%(cate_cd)
    url = f'http://search.cjmall.com/search-web/search/cjmall/categoryItem.json?t=API&o=BEST_SELLING_DESC&sc={cate_cd}' \
          '&s=48&firstSearch=true&listingType=2&isOnload=true&chn=30001001&srcg=true&srbg=true&srfg=true&srp=true&srcb=true'
    # print(url)
    prd = get_prd(url)
    # item_all = prd['result'][0]['rowDatas']
    item_all = [x for x in prd['result'] if x['type'] == 'CJMALL_CATEGORY_ITEM'][0]['rowDatas']
    time.sleep(2)
    return item_all


def get_item(item_all):
    txt_f = open(f'./result/cjmall_{w_date}.jl', 'a', encoding='utf-8')
    # txt_f = open(f'./output/{comp_nm}_{s_cate_cd}_{w_date}.jl', 'a', encoding='utf-8')
    # txt_f_k = open(f'./output/{comp_nm}_{s_cate_cd}_{w_date}.txt', 'a', encoding='utf-8')
    rank = 0
    for i, item in enumerate(item_all):
        try:
            if 'pmgItemImgUrl' in item:
                # 배봄이 대리 요청
                if item['imgUrl'] != '':
                    imgUrl = 'http://thumb.cjmall.net/unsafe/fit-in/470x470/itemimage.cjmall.net' + item['imgUrl']
                else:
                    imgUrl = 'http://thumb.cjmall.net/unsafe/fit-in/470x470/itemimage.cjmall.net/' + \
                             item['pmgItemImgUrl'].split('?')[0]

                itemNm = item['itemNm']
                itemCd = item['itemCd']
                # brandCd = item['brandCd']
                brandNm = item['repBrandNm']
                externCd = item['externCd']
                prd_cd = item['dqId']

                if externCd == '':
                    prd_url = f'http://display.cjmall.com/p/item/{itemCd}'
                else:
                    prd_url = f'http://display.cjmall.com/p/mocode/{externCd}'

                if 'bbsScore' in item:
                    bbsScore = item['bbsScore']
                else:
                    bbsScore = '0'
                if 'bbsCount' in item:
                    bbsCount = item['bbsCount']
                else:
                    bbsCount = '0'

                original_price = int(item['pmgHpSalePrice'])
                if 'pmgSalePrice' in item:
                    sale_price = int(item['pmgSalePrice'])
                else:
                    sale_price = original_price

                # 배봄이 대리 요청
                if original_price == 0:
                    original_price = sale_price

                if 'liveOrderQty' in item:
                    orderQty = item['liveOrderQty']
                else:
                    orderQty = 'Null'  # 배봄이 대리 요청

                rank += 1
                #if original_price
                dc_rate = (original_price-sale_price)/original_price
                result_dic = {}

                result_dic['w_date'] = w_date
                result_dic['comp_nm'] = "CJ홈쇼핑"
                result_dic['comp_cd'] = "CJMALL"
                result_dic['rank_num'] = rank
                result_dic['l_cate_nm'] = m_cate_nm
                result_dic['l_cate_cd'] = str(m_cate_cd)
                result_dic['m_cate_nm'] = s_cate_nm
                result_dic['m_cate_cd'] = str(s_cate_cd)
                #result_dic['s_cate_nm'] = s_cate_nm
                #result_dic['s_cate_cd'] = s_cate_cd
                result_dic['prod_nm'] = itemNm.strip()
                result_dic['itemCd'] = itemCd
                result_dic['brand_nm'] = brandNm
                result_dic['externCd'] = externCd
                result_dic['prod_cd'] = prd_cd
                result_dic['bbsScore'] = bbsScore
                result_dic['bbsCount'] = bbsCount
                result_dic['sale_amt'] = orderQty
                result_dic['s_price'] = sale_price
                result_dic['o_price'] = original_price
                result_dic['dc_rate'] = dc_rate
                result_dic['img_url'] = imgUrl
                result_dic['prod_url'] = prd_url
                result_dic['min_price_yn'] = 'N'

                jl = json.dumps(result_dic)
                txt_f.write(jl + '\n')
                # txt_f_k.write(str(result_dic)+'\n')

        except:
            traceback.print_exc()
            print(i, item)
            break
    txt_f.close()
    # txt_f_k.close()


# headers = {'Host': 'search.CJMALL.com'}

category = json.loads(open('./cate_dic.json', 'r').read())
w_date = datetime.now().strftime("%Y%m%d")
l_cate_nm = '여성의류'
l_cate_cd = category[l_cate_nm]['cd']

l_cate_dic = category[l_cate_nm]['children']
txt_f = open(f'./result/CJmall_{w_date}.jl', 'w', encoding='utf-8')
for m_cate_nm in l_cate_dic.keys():
    m_cate_cd = l_cate_dic[m_cate_nm]['cd']
    m_cate_dic = l_cate_dic[m_cate_nm]['children']
    for s_cate_nm in m_cate_dic.keys():
        s_cate_cd = m_cate_dic[s_cate_nm]['cd']
        sys.stdout.write(f'{s_cate_cd}')
        sys.stdout.flush()
        item_check = True
        while item_check:
            item_all = get_cate(s_cate_cd)
            item_cnt = len(item_all)
            sys.stdout.write(f'\r{s_cate_cd} - {item_cnt}')
            sys.stdout.flush()
            if len(item_all) >= 2:

                get_item(item_all)
                item_check = False
            else:
                print(item_all)
                time.sleep(2)
                item_check = False

print('Complete')


