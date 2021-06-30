import requests
import pandas as pd
import json
from bs4 import BeautifulSoup
import random, time
from itertools import cycle
import datetime
w_date = datetime.datetime.now().strftime("%Y%m%d")
####l_CATE_DIC수집
def get_proxies():  # 프리프록시넷에서 프리프록시들의 리스트를 받아옴
    url = 'https://free-proxy-list.net/'
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/50.0.2661.75 Safari/537.36", }
    r = requests.get(url, headers=header)
    dfs = pd.read_html(r.text, converters={'Port': str})[0]

    https = dfs[dfs['Https'] == 'yes']
    proxies = list(https['IP Address']+':'+https['Port'])
    random.shuffle(proxies)
    return proxies
proxies = get_proxies()
proxy_pool = cycle(proxies)

req_chk = False
try_cnt = 1
url_main = 'https://store.musinsa.com/app/contents/brandshop'
req = requests.get(url_main)


soup = BeautifulSoup(req.text, 'html.parser')
#print(soup)
cate_box = soup.find_all('div', class_="nav_category item_menu_btn")
cate_dic ={}
cate_list =[]
for box in cate_box[:] :
    l_cate_nm = box.find("strong", class_="title").text
    tmp_len = len(box.find_all("ul", class_="nav_category_menu"))
    m_cate_list =[]
    for i in range(0,tmp_len) : 
        tmp_list = box.find_all("ul", class_="nav_category_menu")[i]
        tmp_list2=tmp_list.find_all("li")
        for i in range(0, len(tmp_list2)) :
            m_cate={}
            m_cate['m_cate_cd'] = tmp_list2[i].find("a")['href'].split("/")[4]
            m_cate['m_cate_nm'] = tmp_list2[i].find("a").text.replace("\n",'').replace('\t','').replace('\r','')
            m_cate_list.append(m_cate)
    cate_dic[l_cate_nm] = m_cate_list
    #print(l_cate_nm, l_cate_cd, m_cate_list)

cate_dic2 = {key: value for key, value in cate_dic.items() if key in ['상의','아우터','원피스','바지','스커트']}
print(cate_dic2)
time.sleep(random.randrange(10, 15))
prod_datas=[]


file_path = f'D:/Python/erp3.0/MUSINSA/result/musinsa_Prod_Data_{w_date}.jl'
with open(file_path,'w') as f:
    pass

for l_cate_nm,m_cate_dic in cate_dic2.items() :
    print(l_cate_nm)
    for m_cate in m_cate_dic[:] :
        
        url = 'http://store.musinsa.com/app/svc/get_rank_goods'
        headers = {'connection' : 'keep_alive'}
        formdata = {"page": "1", "rowcnt": 10000, "u_cat_cd": m_cate['m_cate_cd']}
        ###sort 판매순 주간 판매순
        '''
        req_chk = False
        try_cnt = 1
        while req_chk is False and try_cnt <= 10:  # 10번 try
            try:
                req2 = requests.post(url, proxies=proxies, params=formdata)
                #soup = BeautifulSoup(res.text, 'html.parser')
                #var0 = soup.find('ul', class_='n-list-product').find_all('li', class_='prd-block')  # 2019-04-09 페이지 변경
                if req2.status_code == 200:
                    req_chk = True
            except:  # 실패시 재시도
                print("!!Connected Error!! Change the Proxy : try %d" % try_cnt)
                proxies = {"https": next(proxy_pool)}
                #time.sleep(random.randrange(1, try_cnt * 5))
                try_cnt += 1
        
        print("사용프록시 : ",proxies)
        
        #print(req.text[:1000])
        '''

        res = requests.post(url, params = formdata)
        #soup = BeautifulSoup(res.text, 'html.parser')
        prod_json = json.loads(res.text)
        #print(prod_json)
        for prod in prod_json[:] :
            #print(prod)
            prod_data={}
            prod_data['w_date'] = w_date
            prod_data['comp_cd'] = "MUSINSA"
            prod_data['comp_nm'] = "무신사"
            prod_data['l_cate_nm'] = l_cate_nm
            
            prod_data['m_cate_nm'] = m_cate['m_cate_nm'].split("(")[0].strip()
            prod_data['m_cate_cd'] = str(m_cate['m_cate_cd']) ###4자리 >6자리
            prod_data['l_cate_cd'] = str(m_cate['m_cate_cd'])[:3]
            prod_data['prod_cd'] = prod['goods_no']
            prod_data['prod_nm'] = prod['goods_nm'].strip()
            prod_data['brand_cd'] = prod['brand']
            prod_data['brand_nm'] = prod['brand_nm']
            prod_data['o_price'] = int(prod['normal_price'])
            prod_data['s_price'] = int(prod['price'])
            prod_data['dc_rate'] = (prod_data['o_price']-prod_data['s_price'])/prod_data['o_price']
            prod_data['img_url'] = 'https://image.msscdn.net'+ prod['img']
            prod_data['prod_url'] = 'https://store.musinsa.com/app/product/detail/' + prod['goods_no']
            prod_data['avg_est_value'] = prod['avg_est_value'] ##평균별점
            prod_data['est_cnt'] = prod['est_cnt'] 
            prod_data['good_qty'] = prod['good_qty'] ###상품개수
            prod_data['reg_dm'] = prod['reg_dm'] ###상품등록일 추정
            prod_data['gender_cd'] = prod['sex']
            prod_data['rank_num'] = int(prod['rank']) ### 주간 판매량
            prod_data['like_cnt'] = prod['like_cnt']
            prod_data['sale_1y'] = prod['sale_1y']
            prod_data['sale_stat_cl'] = prod['sale_stat_cl']
            #####1년 누적 판매량
            #prod_datas.append(prod_data)
            jl = json.dumps(prod_data)
            with open(file_path,'a') as f:
                f.write(jl+'\n')
        print(m_cate, formdata)
        time.sleep(random.randrange(10, 20))
