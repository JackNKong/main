import requests
import json
import re
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import time, random
##category 수집#########
l_cate_list =['10009097']
w_date = datetime.datetime.now().strftime("%Y%m%d")
#w_date = '20201112'
file_path = f'/root/work/_jeong_jaekeun/erp3.0/NKIDS/result/NKIDS_Prod_Data_{w_date}.jl'
for l_cate in l_cate_list : 
    formdata = {
                        "item.paging.current": "1",
                        # 상품개수 : 100개로 조정
                        "item.paging.rowsPerPage": "100",
                        "item.paging.moreCount": "true",
                        "specialEvent.paging.current": "1",
                        "specialEvent.paging.rowsPerPage": "1",
                        "specialEvent.paging.moreCount": "true",
                        "shoppingNews.paging.current": "1",
                        "shoppingNews.paging.rowsPerPage": "1",
                        "shoppingNews.paging.moreCount": "true",
                        "edm.paging.current": "1",
                        "edm.paging.rowsPerPage": "1",
                        "edm.paging.moreCount": "true",
                        "culture.paging.current":	"1",
                        "culture.paging.rowsPerPage": "1",
                        "culture.paging.moreCount": "true",
                        "bestStore.paging.current": "1",
                        "bestStore.paging.rowsPerPage": "1",
                        "bestStore.paging.moreCount" : "true",
                        "storeNews.paging.current": "1",
                        "storeNews.paging.rowsPerPage": "3",
                        "storeNews.paging.moreCount": "true",
                        "purchaseReview.paging.current":	"1",
                        "purchaseReview.paging.rowsPerPage":	"1",
                        "purchaseReview.paging.moreCount": "true",
                        "cache": "true",
                        "all": "true",
                        "openPetLink": "false",
                        "pageCode": "LIST",
                        #"query": str(cate),
                        "menu": l_cate,
                        "vertical": "KIDS",
                        "sort": "REL_DES",
                        "naverPayOnly": "false",
                        "ios": "false",
                        "sType": "append",
                        "current": "1",
                        "clickCodeArea": "cat"
                    }
    url = f"https://swindow.naver.com/kids/list/category?menu={l_cate}"
    #url ="https://swindow.naver.com/kids/list/more/composite"
    s=requests.Session()
    response = s.post(url,proxies={"http": '125.27.251.206:50817'})
    soup = BeautifulSoup(response.text, 'html.parser')
    #start_num = req_text.find('menuWrapper : $.parseJSON')
    #req_text[start_num:]
    #url = "https://swindow.naver.com/kids/list/more/composit"
    #cate_list = response.findall(class_="list")



    #a = re.findall('<li class="list">(.*?)>', str(response.text))
    tmp_list = soup.find_all("li",class_="list")
    m_cate_dic = []
    for tmp in tmp_list :
        if str(tmp).find('data-type="CATEGORY"') < 0 :
            m_cate={}
            m_cate['m_cate_cd'] = tmp['data-id']
            m_cate['m_cate_nm'] = tmp.find("span").text
            m_cate_dic.append(m_cate)
            #print(m_cate.find("span"))
    print(m_cate_dic)
    
############m_cate고리 리퀘스트 날리기
file_path = f'/erp3.0/NAVER/nkids/result/NKIDS_Prod_Data_{w_date}.jl'
with open(file_path,'w') as f:
    pass
datas=[]
for m_cate in m_cate_dic [11:] :
    print(m_cate['m_cate_nm'])
    m_cate_cd = m_cate['m_cate_cd']
    formdata = {
                    "item.paging.current": "1",
                    # 상품개수 : 100개로 조정
                    "item.paging.rowsPerPage": "100",
                    "item.paging.moreCount": "true",
                    "specialEvent.paging.current": "1",
                    "specialEvent.paging.rowsPerPage": "1",
                    "specialEvent.paging.moreCount": "true",
                    "shoppingNews.paging.current": "1",
                    "shoppingNews.paging.rowsPerPage": "1",
                    "shoppingNews.paging.moreCount": "true",
                    "edm.paging.current": "1",
                    "edm.paging.rowsPerPage": "1",
                    "edm.paging.moreCount": "true",
                    "culture.paging.current":	"1",
                    "culture.paging.rowsPerPage": "1",
                    "culture.paging.moreCount": "true",
                    "bestStore.paging.current": "1",
                    "bestStore.paging.rowsPerPage": "1",
                    "bestStore.paging.moreCount" : "true",
                    "storeNews.paging.current": "1",
                    "storeNews.paging.rowsPerPage": "3",
                    "storeNews.paging.moreCount": "true",
                    "purchaseReview.paging.current":	"1",
                    "purchaseReview.paging.rowsPerPage":	"1",
                    "purchaseReview.paging.moreCount": "true",
                    "cache": "true",
                    "all": "true",
                    "openPetLink": "false",
                    "pageCode": "LIST",
                    #"query": str(cate),
                    "menu": m_cate_cd,
                    "vertical": "KIDS",
                    "sort": "REL_DES",
                    "naverPayOnly": "false",
                    "ios": "false",
                    "sType": "append",
                    "current": "1",
                    "clickCodeArea": "cat"
                }
    url = "https://swindow.naver.com/kids/list/more/composite"
    s=requests.Session()
    response = s.post(url,proxies={"http": '125.27.251.206:50817'},params = formdata )
    soup = BeautifulSoup(response.text, 'html.parser')
    tmp_list =soup.find_all("li", class_="list")
    #print(response.text)
    #print("------------------")
    #tmp_list[:10]
    prod_list=[]
    for tmp in tmp_list :
        if tmp.find("dl", class_="goods_desc") and not(tmp.find("div",class_="price soldout")): 
            prod_list.append(tmp)
    #    <dl class="goods_desc">
    print(len(prod_list))
     
    #prod_list[0:2]
    
    ####인기순####
    rank=1
    for prod in prod_list:
        data ={}
        img_url = prod.find("img")['src']
        #prod_url = prod.find("a", class_="link")['href']
        data['w_date'] = w_date
        data['comp_cd'] = "NAVER_KIDS"
        data['comp_nm'] = "네이버키즈"
        data['l_cate_cd'] = "10009097"
        data['l_cate_nm'] = "키즈패션"
        data['m_cate_cd'] = str(m_cate_cd)
        data['m_cate_nm'] = m_cate['m_cate_nm']
        data['brand_nm'] = prod.find('dt',class_="title").text
        tmp_num1 = prod.find("a", class_="link")['class'][1].find("i:")
        tmp_num2 = prod.find("a", class_="link")['class'][1].find("r:")
        prod_cd = prod.find("a", class_="link")['class'][1].split(",")[1]
        data['prod_cd'] = str(re.findall("\d+",prod_cd)[0])
        data['prod_nm'] = prod.find("dt",class_="tit").text.strip()
        data['rank_num'] = rank
        s_price = int(prod.find("strong").text.replace("원",'').replace(",",''))
        data['s_price'] = s_price
        data['o_price'] = None
        #data['o_price'] = int(prod.find("strong").text.replace("원",'').replace(",",''))
        dc_rate_tmp = prod.find("span",class_="blind")
        
        if dc_rate_tmp == None :
            dc_rate= 0
        else :
            dc_rate = int(prod.find("span",class_="blind").text.replace("%",""))/100
        
        #print(dc_rate)
        data['dc_rate'] = dc_rate
        #data['dc_rate'] = 0
        #data['o_price'] = int(round(s_price/(1-dc_rate),-2))
        prod_url =prod.find("a", class_="link")['href']
        data['prod_url'] = prod_url = re.compile('(.+products\/\d+)').findall(prod_url)[0]
        data['img_url'] = img_url.split("?")[0]
        
        rank=rank+1
        
        ####부가 가능목록
        ###스토어코드, 찜수, 찜
        #datas.append(data)
        jl = json.dumps(data)
        with open(file_path,'a') as f:
            f.write(jl+'\n')
        time.sleep(random.randrange(1, 2))

#df=pd.DataFrame(datas)
#df.head(2)
#df.to_json(f'/root/work/_jeong_jaekeun/erp3.0/NKIDS/result/NKIDS_Prod_Data_{w_date}.jl', orient = 'records')