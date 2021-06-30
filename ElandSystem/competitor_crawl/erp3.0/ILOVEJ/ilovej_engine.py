import re
import time
from datetime import datetime
from itertools import cycle
import sys
import requests
from bs4 import BeautifulSoup
from lxml.html import fromstring
import json
import time, random
w_date = datetime.now().strftime("%Y%m%d")
prod_f = open(f"D:/Python/erp3.0/ILoveJ/result/ilovej_Prod_Data_%s.jl" % w_date, 'w', encoding='utf-8')
#### l_cate_list 만들기

url = 'http://www.ilovej.net/index.html'
req = requests.get(url, proxies={"3128":'140.227.199.112'})
soup = BeautifulSoup(req.content, 'html.parser')
cate_list = soup.find("ul", class_="lnb-cate").find_all("li")
#cate_list = [i.find_all("span")[0] for i in cate_list]
fin_cate_list =[]
for cate in cate_list :
    data ={}
    if cate.find("span") is not None :
        data['l_cate_link'] = cate.find('a')['href']
        data['l_cate_nm'] = cate.find_all("span")[0].text
        data['l_cate_cd'] = cate.find('a')['href'].split("xcode=")[1].replace("&type=Y","")
        data['m_cate_dic'] = []
        #data['m_cate_cd'] = None
        #data['m_cate_nm'] = None
    #print(len(cate.find("span")))
        fin_cate_list.append(data)

l_cate_list = [i for i in fin_cate_list if i['l_cate_nm'] in ['OUTER','PANTS','TOP','SKIRT','DRESS','SET','LEGGINGS']]

#####m_cate를 l_cate하위로 담기###
for cate in l_cate_list :
    url = "http://www.ilovej.net" + cate['l_cate_link']
    req = requests.get(url, proxies={"3128": '140.227.199.112'})
    soup = BeautifulSoup(req.content, 'lxml')
    box = soup.find('div',class_="class-list")
    m_cate_list = box.find_all("a")
    for m_cate in m_cate_list :
        tmp_cate = {}
        tmp_cate['m_cate_link'] = m_cate['href']
        tmp_cate['m_cate_nm'] = m_cate.text
        tmp_cate['m_cate_cd'] = m_cate['href'].split('mcode=')[1]
        cate['m_cate_dic'].append(tmp_cate)
    time.sleep(random.randrange(1, 3))
print(l_cate_list)


for l_cate in l_cate_list :
    # m_cate_list = l_cate['m_cate_dic']
    # for m_cate in m_cate_list :
    url = "http://www.ilovej.net" + l_cate['l_cate_link']
    req = requests.get(url, proxies={"3128": '140.227.199.112'})
    soup = BeautifulSoup(req.content, 'lxml')
    item_list = soup.find_all('dl', class_ ="item-list")
    print(l_cate)
    rank = 1
    for item in item_list :
        data = {}
        data['w_date'] = w_date
        data['rank_num'] = rank
        data['l_cate_cd'] = "KIDS"
        data['l_cate_nm'] = "KIDS"
        data['m_cate_cd'] = str(l_cate['l_cate_cd'])
        data['m_cate_nm'] = str(l_cate['l_cate_nm'])
        data['brand_nm'] = "아이러브제이"
        data['comp_nm'] = "아이러브제이"
        data['comp_cd'] = "ILOVEJ"
        data['prod_nm'] = item.find('li',class_='prd-name').text.strip()

        if item.find("strike") is not None :
            data['o_price'] = int(item.find("strike").text.replace("won","").replace(",","").strip())
            data['s_price'] = int(item.find_all('li',class_="prd-price")[1].text.replace("won","").replace(",","").strip())
        else :
            data['o_price'] = int(item.find('li', class_="prd-price").text.replace("won","").replace(",","").strip())
            data['s_price'] = data['o_price']
        data['dc_rate'] = (data['o_price']- data['s_price'])/data['o_price']
        print(data['prod_nm'],data['o_price'], data['s_price'],data['dc_rate'])
        data['img_url'] = "http://www.ilovej.net" + item.find("img")['src'].split("?")[0]
        prod_url = "http://www.ilovej.net" + item.find("a")['href']
        data['prod_url'] =re.compile('(.+branduid=\d+)').findall(prod_url)[0]
        data['prod_cd'] = data['prod_url'].split("branduid=")[1].split("&")[0]
        prod_f.write(json.dumps(data) + '\n')
        rank +=1
    time.sleep(random.randrange(1, 2))