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
headers1 = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection': 'keep-alive',
'Cookie': 'ga=GA1.3.1874134317.1604281774; c3R5bGVub3JpdGVyX3NwbV9tZW1iZXJfaWRfcGM%3D=1832de8ce267d616bc9ff32f0cb6efb0; snap_spm459_idsyncstatus=; STYLENORITER.co.kr-crema_device_token=iMZHbSeg6iu8dTJt; CUK45=cuk45_stylenoriter_af8b23e5f7c4ae04b9d852c306b243d9; CUK2Y=cuk2y_stylenoriter_af8b23e5f7c4ae04b9d852c306b243d9; _fbp=fb.2.1604281777838.221509822; _wp_uid=2-f6d589c1a850e6862d5bf7d2e09b9dc1-s1580689719.833|windows_10|chrome-tjcdnz; TR10104105155_t_uid=49125349016018017.1604476487164; recent_plist=9494%7C1663%7C9495%7C9578%7C9581%7C8364; _gid=GA1.3.1610709350.1606195092; ECSESSID=174d4d7a35a81992fedd7827ea3e412c; basketcount_1=0; basketprice_1=0%EC%9B%90; wish_id=a3fabb4a9c304abaf25aad51405e2936; wishcount_1=0; isviewtype=pc; _efpn=0e0d6cdf62aea19272351a8b54f0ad36_d87b-46d5; _gat_UA-41324984-1=1; _gat_gtag_UA_41324984_1=1; wcs_bt=s_29f56ccd44c3:1606195425',
'Host': 'STYLENORITER.co.kr',
'Referer': 'http://stylenoriter.co.kr/index.html',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}
main_url = "http://stylenoriter.co.kr/exec/front/Product/SubCategory"
req = requests.get(main_url , headers = headers1)
#print(req)
soup_list = json.loads(req.text)
#print(soup)
l_cate_dic ={'24':'TOP&KNIT','25' : 'BOTTOM','27' : 'DRESS&SET'}
l_cate_cd_list = set(l_cate_dic.keys())
print(l_cate_cd_list)
cate_list=[]
# for soup in soup_list :
#     if str(soup['parent_cate_no']) in l_cate_cd_list :
#         data={}
#         data['l_cate_cd'] = soup['parent_cate_no']
#         data['m_cate_cd'] = soup['cate_no']
#         data['m_cate_nm'] = soup['name']
#         cate_list.append(data)
#     else : pass
print(cate_list)
time.sleep(random.randrange(1, 5))
prod_f = open(f"D:/Python/erp3.0/STYLENORITER/result/stylenoriter_Prod_Data_%s.jl" % w_date, 'w', encoding='utf-8')
for l_cate_cd, l_cate_nm in l_cate_dic.items() :
    prod_data={}
    url = f"http://stylenoriter.co.kr/category/{l_cate_nm}/{l_cate_cd}/"
    req = requests.get(url, proxies={"3128": '27.133.232.98'}, headers= headers1)
    soup = BeautifulSoup(req.text, 'html.parser')
    print(url)
    container = soup.find('div', class_='xans-element- xans-product xans-product-listnormal ec-base-product')
    ul = container.find("ul", class_='prdList grid4')
    prod_list = ul.find_all('li', class_="xans-record-")
    print(len(prod_list))
    prod_datas = []
    rank_num = 1
    for i in prod_list:
        if i.find("div", class_='thumbnail') is not None:
            prod_data ={}
            prod_data['w_date'] = w_date
            prod_data['comp_cd'] = 'STYLENORITER'
            prod_data['comp_nm'] = '스타일노리터'
            prod_data['brand_nm'] = '스타일노리터'
            prod_data['l_cate_cd'] = "KIDS"
            prod_data['l_cate_nm'] = "KIDS"
            prod_data['m_cate_cd'] = l_cate_cd
            prod_data['m_cate_nm'] = l_cate_nm
            prod_data['img_url'] =  "http:" + i.find('img')['src'].split("?")[0]
            prod_data['rank_num'] = rank_num
            contents = i.find('p', class_="name")
            prod_url = 'https://www.stylenoriter.co.kr/' + contents.find('a')['href']
            prod_data['prod_url'] = re.compile('(.+product_no=\d+)').findall(prod_url)[0]
            prod_data['prod_nm'] = contents.find_all('span')[2].text
            prod_cd = str(re.search('product_no=(.+?)&', contents.find('a')['href']).group(0)).replace("product_no=","").replace("&","")
            prod_data['prod_cd'] = prod_cd
            print(prod_data['rank_num'],prod_data['prod_nm'])
            s_price = i.find('li', rel='판매가')
            if s_price is not None :
                prod_data['s_price'] = int(s_price.find_all("span")[1].text.replace(',','').replace('원',''))
                prod_data['o_price'] = int(s_price.find_all("span")[1].text.replace(',', '').replace('원', ''))
            else : prod_data['s_price'] = None

            o_price = i.find('li', rel='할인판매가')
            if o_price is not None:
                prod_data['s_price'] = int(o_price.find_all("span")[1].text.replace(',','').replace('원',''))
            elif re.findall("소비자가", prod_data['prod_nm']) :
                prod_data['o_price'] = int(prod_data['prod_nm'].split("소비자가 :")[1].replace(',','').replace('원',''))
                prod_data['prod_nm'] = prod_data['prod_nm'].split("소비자가 :")[0]
            else : pass
            prod_data['dc_rate'] = round(float((prod_data['o_price'] - prod_data['s_price']) / prod_data['o_price']),2)
            #print(prod_data['dc_rate'])

            prod_summary = i.find('li', rel='상품 요약설명')
            if prod_summary is not None:
                prod_data['prod_summary'] = prod_summary.find_all("span")[1].text
            else: prod_data['prod_summary'] = None

            color_cd = i.find('li', rel='상품색상')
            if color_cd is not None:
                prod_data['color_cd'] = color_cd.find("span", class_='chips')['title']
            else: prod_data['color_cd'] = None

            prod_datas.append(prod_data)
            prod_f.write(json.dumps(prod_data) + '\n')
            rank_num +=1
        else : pass
    time.sleep(random.randrange(1, 5))


####예외처리 ###26 : OUTER 예외처리
l_cate_dic2 ={'26': 'OUTER'}
l_cate_cd_list = set(l_cate_dic.keys())
url = f"http://stylenoriter.co.kr/category/DRESS&SET/26/"
req = requests.get(url, proxies={"3128": '27.133.232.98'}, headers= headers1)
soup = BeautifulSoup(req.text, 'html.parser')
print(url)

thum_list = soup.find_all('div', class_="thumbnail")
des_list = soup.find_all('div', class_ = "description")
###개수맞는지 검사
if len(thum_list) == len(des_list) :
    pass
else : print("error")
rank_num=1

for thum,des in zip(thum_list[5:],des_list[5:]):
    prod_data ={}
    prod_data['w_date'] = w_date
    prod_data['comp_nm'] = 'STYLENORITER'
    prod_data['brand_nm'] = '스타일노리터'
    prod_data['l_cate_cd'] = "KIDS"
    prod_data['l_cate_nm'] = "KIDS"
    prod_data['m_cate_cd'] = "26"
    prod_data['m_cate_nm'] = 'OUTER'
    prod_data['img_url'] =  "http:" + thum.find('img')['src'].split("?")[0]
    prod_data['rank_num'] = rank_num
    contents = des.find('p', class_="name")
    prod_data['prod_url'] = 'https://www.stylenoriter.co.kr/' + contents.find('a')['href']
    prod_data['prod_nm'] = contents.find_all('span')[2].text.strip()
    prod_cd = str(re.search('product_no=(.+?)&', contents.find('a')['href']).group(0)).replace("product_no=","").replace("&", "")
    prod_data['prod_cd'] = prod_cd
    print(prod_data['rank_num'],prod_data['prod_nm'])
    s_price = des.find('li', rel='판매가')
    if s_price is not None :
        prod_data['s_price'] = int(s_price.find_all("span")[1].text.replace(',','').replace('원',''))
        prod_data['o_price'] = int(s_price.find_all("span")[1].text.replace(',', '').replace('원', ''))
    else : prod_data['s_price'] = None

    o_price = des.find('li', rel='할인판매가')
    if o_price is not None:
        #print(o_price,"________________________________________________________")
        prod_data['s_price'] = int(o_price.find_all("span")[1].text.replace(',','').replace('원',''))
    else : pass
    prod_data['dc_rate'] = round(float((prod_data['o_price'] - prod_data['s_price']) / prod_data['o_price']),2)
    #print(prod_data['dc_rate'])
    prod_summary = des.find('li', rel='상품 요약설명')
    if prod_summary is not None:
        prod_data['prod_summary'] = prod_summary.find_all("span")[1].text
    else: prod_data['prod_summary'] = None

    color_cd = des.find('li', rel='상품색상')
    if color_cd is not None:
        prod_data['color_cd'] = color_cd.find("span", class_='chips')['title']
    else: prod_data['color_cd'] = None

    prod_datas.append(prod_data)
    prod_f.write(json.dumps(prod_data) + '\n')
    rank_num +=1

time.sleep(random.randrange(1, 5))
