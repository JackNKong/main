import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import random


##카테고리 수집
url = 'https://starngage.com/app/global/influencer/ranking/korea'
res = requests.get(url,headers = headers, proxies = {"http": '125.27.251.206:50817'})
soup = BeautifulSoup(res.text, 'html.parser')
cate_list = soup.find('select',id = 'topic', class_='custom-select mr-sm-2').find_all('option')

url_list = []
cate_list_2= cate_list[:13] +cate_list[14:]
for cate in cate_list_2[:] :
    #print(cate)
    tmp_dic={}
    url2 = 'https://starngage.com/app/global/influencer/ranking/korea/' + cate['value']
    print(url2)
    #proxies = {"http": '125.27.251.206:50817'}
    res2 = requests.get(url2, headers =headers)
    soup2 = BeautifulSoup(res2.text, 'html.parser')
    tmp_list = soup2.find('ul',class_ = 'pagination justify-content-center').find_all('a')
    tmp_dic['url'] = url2
    tmp_dic['len_url'] = len(tmp_list)
    url_list.append(tmp_dic)
    time.sleep( random.uniform(1,3) )

datas = []

for url_dic in url_list[:]:
    for i in range(0, 11):
        # print(url_dic['url'] +'?page=' + str(i))
        url = url_dic['url'] + '?page=' + str(i)
        print(url)
        # url = 'https://starngage.com/app/global/influencer/ranking/korea/architecture?page=0'
        # proxies = {"http": '125.27.251.206:50817'}
        try:
            res = requests.get(url, headers=headers)
            soup = BeautifulSoup(res.text, 'html.parser')
            time.sleep(random.uniform(1, 4))

            table_box = soup.find('table', class_='table table-hover table-responsive-sm').find('tbody')
            item_box = table_box.find_all('tr')
            for item in item_box[:]:
                tmp_dic = {}
                # print(item)
                td_list = item.find_all('td', class_='align-middle')
                tmp_dic['rank_num'] = td_list[0].text
                influnecer_text = td_list[2].text
                tmp_dic['influencer_nm'] = influnecer_text.split("@")[0]
                tmp_dic['influencer_id'] = "@" + influnecer_text.split("@")[1].replace("\n", "")
                tmp_dic['hashtag'] = td_list[4].text.split("\n")[1:]
                tmp_dic['followers'] = td_list[5].text
                tmp_dic['engagement_rate'] = td_list[6].text
                datas.append(tmp_dic)
        except:
            print('error', url)

df = pd.DataFrame(datas)

def fashion_T (list_) :
    if "Fashion" in list_ : return True
    else : return False

df['fashion_T'] = df['hashtag'].apply(fashion_T)
df['stargage_url']  = 'https://starngage.com/app/global/influencers/' + df['influencer_id']
df['stargage_url'] = df['stargage_url'].apply(lambda x: x.replace("@",""))
df

