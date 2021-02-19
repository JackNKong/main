import requests
import json
import pandas as pd
from bs4 import  BeautifulSoup
youtube_url = 'https://www.youtube.com/channel/UC5z2fxN6rs69cSyXur6X6Mg'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': '__cfduid=d6ef54cdffd1565fbe3ca5f21ccaace441613609797; PHPSESSXX=938ln85pjc8ptjkj0cmdq1u43o; __asc=d71d1c92177b2a38d4d56774aeb; __auc=d71d1c92177b2a38d4d56774aeb; _ga=GA1.2.586638137.1613609799; _gid=GA1.2.1780472495.1613609799; __qca=P0-457368395-1613609799273; _pbjs_userid_consent_data=3524755945110770; _pubcid=f6296823-00d0-4a05-9c27-b9e0b277dc1c; _fbp=fb.1.1613609800473.833446137; pbjs-unifiedid=%7B%22TDID%22%3A%22666cdcca-6777-4062-9753-283b5f20f80d%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222021-01-18T00%3A56%3A41%22%7D; __gads=ID=e311e7bd667cf490:T=1613609801:S=ALNI_MYPjy2rvRbfPqr-oZGxSVAvQQmxMQ; id5_storage=%7B%22created_at%22%3A%222021-02-18T00%3A56%3A42.652Z%22%2C%22id5_consent%22%3Atrue%2C%22original_uid%22%3A%22ID5-ZHMOcQ75LPgFgqJ6S5LNwLpDz8qVnGVtzcWuXwsgYg%22%2C%22universal_uid%22%3A%22ID5-ZHMOzJsd57yzjbJ5pyik17rQOUdkZOQYxPzYe15v1g%22%2C%22signature%22%3A%22ID5_AYCSsObl4H837Vp_8lu2YWQAX8UgN6J8u73B4mnbE6o1jBoh9jms2OGI3H3Y4V_Sk9O4ZAymyMd7pkMm1f6BoH4%22%2C%22link_type%22%3A2%2C%22cascade_needed%22%3Atrue%7D; _cb_ls=1; _cb=BvnE_E5ZfAvD0vzj5; cf_clearance=9ce391b1eeb1b006b737702f4f03cfdf5e38bac2-1613609866-0-150; _cb_svref=null; lngtd-sdp=21; _gat_socialblade=1; cto_bidid=N8j07V84bUxnYXJNZ1c2UUxKUWh3RDAyQzRIck1WVFBkRFhFcGtnMXFWSG1DZnoyNmpWbkdNSjlvN2d0dHhzUFhEeEtobXBoeXBjJTJCMkR6V2VSWFAzRVduY2R0ak5tTjAlMkZsZXlhV0x2Qnc0Q1RvN1Q0RW5vNVJ3TTRrT2IlMkJCVUNDdks3Sg; cto_bundle=VIEAa19ZQlZ6amlScUxMOSUyQmdvbmJ6aDVYaSUyQlMzMkRwdFcyVnF0U2RHaGNmUUJuSVY0VVYwSzhYcGxiMURENWN6Vk9PVE1zbEV4dzBNZlFLJTJGMGU5Vmw2S2tyREhiJTJGS2ZKMHZJQXNxOVFUeWNiS2RWRkxiWGl5ME5aajNJd3Mzb0hpc0V4SjZTTlZ1N2VsSVlSVUJzUjRvcTV0QSUzRCUzRA; _gat_gtag_UA_137034616_3=1; _lr_retry_request=true; _chartbeat2=.1613609833234.1613613764683.1.Ba5h5FCogC9DB7EGbKCahsS4BM1sPF.2',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}


url_list=['https://www.youtube.com/channel/UC5z2fxN6rs69cSyXur6X6Mg']  ##탱구티비
datas =[]
for youtube_url in url_list :
    socialblade_url = youtube_url.replace('www.youtube.com','socialblade.com/youtube')
    #'https://socialblade.com/youtube/channel/UC5z2fxN6rs69cSyXur6X6Mg'
    res = requests.get(socialblade_url,headers=headers,proxies={'http': '125.27.251.206:50817'})
    soup=BeautifulSoup(res.text,'html.parser')
    infobox = soup.find('div',id = 'YouTubeUserTopInfoWrap')
    databox = soup.find('div', id = 'socialblade-user-content')
    tmp_dic ={}
    tmp_dic['title']=infobox.find('h1').text
    info_list = infobox.find_all('div',class_='YouTubeUserTopInfo')
    databox = databox.find_all('div')[4]
    data_list = databox.find_all('p')
    if len(info_list) ==6 :
        #for info in info_list:
        tmp_dic['uploads']=info_list[0].find_all('span')[1].text
        tmp_dic['subscribers']=info_list[1].find_all('span')[1].text
        tmp_dic['view_cnt']=info_list[2].find_all('span')[1].text
        tmp_dic['country']=info_list[3].find_all('span')[1].text
        tmp_dic['created_date']=info_list[5].find_all('span')[1].text
        #datas.append(tmp_dic)
        #print(info.find_all('span')[1].text)
    else :
        tmp_dic['uploads']='none page'
        tmp_dic['subscribers']='none page'
        tmp_dic['view_cnt']='none page'
        tmp_dic['country']='none page'
        tmp_dic['created_date']='none page'
        #datas.append(tmp_dic)


    if len(data_list) == 5 :
        tmp_dic['socialblade_rank_num'] = data_list[0].text
        tmp_dic['subscriber_rank_num'] = data_list[1].text
        tmp_dic['video_cnt_rank'] = data_list[2].text
        tmp_dic['country_rank_num'] = data_list[3].text
        tmp_dic['people_rank_num'] = data_list[4].text
        datas.append(tmp_dic)
    else :
        tmp_dic['socialblade_rank_num'] ='none page'
        tmp_dic['subscriber_rank_num'] = 'none page'
        tmp_dic['video_cnt_rank'] ='none page'
        tmp_dic['country_rank_num'] = 'none page'
        tmp_dic['people_rank_num'] ='none page'
        datas.append(tmp_dic)
df=pd.DataFrame(datas)