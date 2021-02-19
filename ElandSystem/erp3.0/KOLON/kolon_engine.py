# 카테고리 정보 수집
from datetime import datetime
import requests
import json
import sys
import time, random



l_cate_dic = {'Women':'133010020000','Men':'133010010000'}
cate_dic = {}

for l_cate_nm in l_cate_dic:
    l_cate_cd = l_cate_dic[l_cate_nm]
    cate_dic[l_cate_nm] = {}
    cate_dic[l_cate_nm]['cate_cd'] = l_cate_cd
    cate_dic[l_cate_nm]['children'] = {}
    
    url = f'https://www.kolonmall.com/View/{l_cate_nm}'
    r=requests.get(url)
    cate_text = r.text
    cate_text = cate_text[cate_text.find(f',"category:{l_cate_cd}"'):cate_text.find('"category"},"$ROOT_QUERY')]
    cate_text = '{' + cate_text[1:] + '"category"}}'    
    
    cate_jl = json.loads(cate_text)
    
    for ct in cate_jl:
        m_cate_nm = cate_jl[ct]['name']
        m_cate_cd = cate_jl[ct]['id']
        if m_cate_cd != l_cate_cd:
            cate_dic[l_cate_nm]['children'][m_cate_nm] = {'cate_cd':m_cate_cd}
        
print(cate_dic)
time.sleep(5)

# 상품 정보 수집
w_date = datetime.now().strftime("%Y%m%d") 
file_path = f'D:/Python/erp3.0/KOLON/output/KOLON_Prod_Data_{w_date}.jl'

def parse_item(js,page):
    prd_list = js['results']
    for i, item in enumerate(prd_list):
        result_dic = {}
        result_dic['comp_nm']  = '코오롱몰'
        result_dic['comp_cd'] = 'KOLON'
        result_dic['l_cate_cd'] = l_cate_cd
        result_dic['l_cate_nm'] = l_cate_nm
        result_dic['m_cate_cd'] = m_cate_cd            
        result_dic['m_cate_nm'] = m_cate_nm
        result_dic['brand_nm']  = item['supplierBrandName']
        result_dic['prod_cd']   = item['code']
        result_dic['prod_nm']   = item['name'].strip()
        result_dic['rank_num']  = i + 1 + ((page-1)*100)
        result_dic['s_price']   = int(item['price']['price'])
        result_dic['o_price']   = int(item['price']['wishPrice'])
        #20201126정재근 수정
        
        result_dic['dc_rate'] = (result_dic['o_price']- result_dic['s_price'] )/result_dic['o_price']
        #result_dic['dc_rate']   = item['price']['discountRate']
        result_dic['prod_url']   = 'https://www.kolonmall.com/Product/' + item['code']
        result_dic['img_url']   = item['representationImage']            

        result_dic['supplierBrandCode']   = item['supplierBrandCode']
        result_dic['supplierCode']        = item['supplierCode']            
        result_dic['supplierName']        = item['supplierName']
        result_dic['produceYear']         = item['produceYear']
        result_dic['season']              = item['season']
        result_dic['color']               = item['color']
        result_dic['sellingPoint']        = item['sellingPoint']
        result_dic['rolloverImage']       = item['rolloverImage']
        result_dic['w_date'] = w_date
        jl = json.dumps(result_dic)
        with open(file_path,'a') as f:
            f.write(jl+'\n')
#cate_dic = {'Women': {'cate_cd': '133010020000', 'children': {'슈즈': {'cate_cd': '133010071600'}, '가방/지갑': {'cate_cd': '133010071700'}, '액세서리': {'cate_cd': '133010071800'}, '쥬얼 리': {'cate_cd': '133010072000'}, '라이프웨어': {'cate_cd': '133010021900'}}}, 'Men': {'cate_cd': '133010010000', 'children': {'티셔츠': {'cate_cd': '133010061100'}, '셔츠': {'cate_cd': '133010061200'}, '니트': {'cate_cd': '133010061300'}, '팬츠': {'cate_cd': '133010061400'}, '아우터': {'cate_cd': '133010061500'}, '수트': {'cate_cd': '133010061600'}, '슈즈/가방': {'cate_cd': '133010061700'}, '액세서리': {'cate_cd': '133010061900'}, '그루밍': {'cate_cd': '133010012000'}, '언더웨어': {'cate_cd': '133010012100'}}}}
for l_cate_nm in cate_dic:
    l_cate_cd = cate_dic[l_cate_nm]['cate_cd']
    m_cate_dic = cate_dic[l_cate_nm]['children']
    
    for m_cate_nm in m_cate_dic:
        m_cate_cd = m_cate_dic[m_cate_nm]['cate_cd']
        print(m_cate_cd, m_cate_nm)
        page = 1
        url = f'https://www.kolonmall.com/Product/Search?category={m_cate_cd}&pageNumber={page}&sort=best-desc&perPage=100'
        r=requests.get(url)
        js = json.loads(r.content)
        totalCount = js['page']['totalCount']
        total_page = (totalCount//100) + 1
        
        parse_item(js,page)        
        sys.stdout.write(f'\r{l_cate_nm} - {m_cate_nm} | {page} / {total_page}                     ')
        sys.stdout.flush()
        time.sleep(1)
        
        for page in range(2,total_page+1):
            url = f'https://www.kolonmall.com/Product/Search?category={m_cate_cd}&pageNumber={page}&sort=best-desc&perPage=100'
            r=requests.get(url)
            js = json.loads(r.content)
            parse_item(js,page)
            sys.stdout.write(f'\r{l_cate_nm} - {m_cate_nm} | {page} / {total_page}                     ')
            sys.stdout.flush()
            time.sleep(random.randrange(1, 4))

print('\nComplete.')