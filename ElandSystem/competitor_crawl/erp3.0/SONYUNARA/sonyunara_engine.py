import json
#from datetime import datetime
import pandas as pd
import requests
import scrapy
from bs4 import BeautifulSoup
import datetime
import re
import time, random
w_date = datetime.datetime.now().strftime('%Y%m%d')
prod_f = open(f"D:/Python/erp3.0/SONYUNARA/result/sonyunara_Prod_Data_%s.jl" % w_date, 'w', encoding='utf-8')
#prod_url_f = open(f"./result/sonyunara_prod_url_%s.jl" % w_date, 'w', encoding='utf-8')
#none_prod_url_f = open(f"./result/sonyunara_non_sale_prod_url_%s.jl" % w_date,'w', encoding='utf-8')
###중분류로 브랜드 아우터#### > 
'''
cate_list = {
        "010401": "가디건·조끼",
        "010403": "야상·점퍼 ","010405" : "패딩",
        "010404": "자켓·코트 ","010406": "플리스",
        "010102": "긴팔티셔츠 ","010104": "맨투맨 ","010103": "후드 ","010101": "반팔/민소매티셔츠","010105": "니트",
        "010201": "셔츠","010202": "블라우스","0105": "All","040701": "상의","040702": "하의","0103": "원피스",
        "0202": "스커트","020101": "숏팬츠","020102": "롱팬츠","020103": "청바지","020104": "면바지","020105": "레깅스",
        "020106": "슬랙스","060101": "백팩·스쿨백","060102": "가방","050101": "운동화·단화","050102": "구두·워커 ",
        "050103": "샌들·슬리퍼·장화","070101": "주얼리","070104": "모자·벨트","070105": "양말·스타킹","3101": "선오픈"
    }
'''

#####l_cate리스트만들기#############
main_url = "https://www.sonyunara.com/"
s = requests.Session()
res=s.get(main_url, proxies={"3128": '27.133.232.98'})
dom = BeautifulSoup(res.content, "html.parser")
li_a_list=dom.find_all("a")
l_cate_list={}
for li_a in li_a_list : 
    tmp_txt=str(li_a)
    if tmp_txt.find("/shop/list.php?cate=") == 9 and tmp_txt.find("target") == -1: 
        num= re.findall("\d+",tmp_txt)
        if len(num[0]) ==4 :
            l_cate_list[num[0]] = tmp_txt.split(">")[1].replace("</a","")
####소나라벨 특수 페이지 삭제
del l_cate_list['0301']
del l_cate_list['3701']
del l_cate_list['3704']
###l_cate를 넣어 m_cate request돌리고 상품정보 얻기
datas=[]
for l_cate_cd in l_cate_list.keys():
    l_cate_nm = l_cate_list[l_cate_cd]
    url = f'https://www.sonyunara.com/shop/list.php?cate={l_cate_cd}'
    s=requests.Session()
    response=s.get(url, proxies={"3128": '27.133.232.98'})
    dom = BeautifulSoup(response.content , "html.parser")
    # tmp_list = dom.select(".tabmenu > li")
    m_cate_list=[]
    # for tmp in tmp_list :
    #     tmp = str(tmp)
    #     num = re.findall("\d+",tmp)
    #     m_cate_list.extend(num)
    # #print(l_cate_nm,"중카테고리 : ",m_cate_list)
    # for m_cate_cd in m_cate_list:
    #     url = f'https://www.sonyunara.com/shop/list.php?cate={m_cate_cd}'
    #     s=requests.Session()
    #     response=s.get(url, proxies={"3128": '27.133.232.98'})
    #     dom2 = BeautifulSoup(response.content , "html.parser")
    #l_cate_nm = "KIDS"
    m_cate_nm = l_cate_nm
    elements = dom.select("div > div > div > div > div > ul > li")

    for i in range(7,len(elements)) :
        tmp_data ={}
        tmp_data['comp_cd'] = 'SONYUNARA'
        tmp_data['comp_nm'] = '소녀나라'
        tmp_data['w_date'] = w_date
        tmp_data['l_cate_nm'] = "KIDS"
        tmp_data['l_cate_cd'] = "KIDS"
        tmp_data['m_cate_nm'] = m_cate_nm
        tmp_data['m_cate_cd'] = str(l_cate_cd)
        tmp_data['brand_nm'] = "소녀나라"
        #tmp_data['prod_nm'] = elements[i].select_one(".subject").text.strip().replace("[","").replace("]","")  20201123
        tmp_data['prod_nm'] = elements[i].select_one(".subject").text.strip()
        tmp_data['rank_num'] = int(i-6)
        tmp_list = elements[i].select(".pull-left")[0].text.split("%")
        if len(tmp_list) == 2 :
            tmp_data['dc_rate'] = int(tmp_list[0].replace("\n",""))/100
            tmp_data['s_price'] =int(tmp_list[1].replace("\n","").replace(",",""))
        else :
            tmp_data['dc_rate'] = 0
            tmp_data['s_price'] =int(tmp_list[0].replace("\n","").replace(",",""))
        tmp_data['o_price'] = None
        tmp_data['prod_url'] = "https://www.sonyunara.com/" + elements[i].select_one("a")["href"]
        tmp_url = elements[i].find("img")["src"]
        if tmp_url[:4] == "http" :
            tmp_data['img_url' ] = tmp_url
        else : tmp_data['img_url' ] = "http:"+ elements[i].find("img")["src"]
        tmp_data['prod_cd'] = elements[i].find("img")["src"].split("/")[5]
        datas.append(tmp_data)
        #else : tmp_data['pur_cnt'] = 0

        prod_f.write(json.dumps(tmp_data) + '\n')
    print(m_cate_nm)
    time.sleep(random.randrange(1, 2))

    
    
    