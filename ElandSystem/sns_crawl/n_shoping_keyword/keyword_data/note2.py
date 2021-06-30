import requests
from bs4 import BeautifulSoup as bs
import json
import numpy as np
import datetime
import time
import sys
import os, random
import pandas as pd


def get_data(src_str, basedate, output_file):
    startDate = basedate[:6]
    endDate = datetime.date.today().strftime('%Y%m')

    headers = {'Referer': 'https://datalab.naver.com/'
        , 'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    url = 'http://datalab.naver.com/qcHash.naver'
    formdata = {'queryGroups': src_str
        , 'startDate': startDate, 'endDate': endDate, 'timeUnit': 'week'
        , 'gender': '', 'age': '', 'device': ''}

    r = requests.post(url, headers=headers, data=formdata)
    hash_data = json.loads(r.text)
    hashKey = hash_data['hashKey']
    # print(hash_data)

    trend_url = f'http://datalab.naver.com/keyword/trendResult.naver?hashKey={hashKey}'
    # print(trend_url)
    r = requests.get(trend_url, headers=headers)
    soup = bs(r.text, 'lxml')
    graph_raw = soup.find('div', id='graph_data').get_text()
    # graph = json.loads(soup.find('div',id = 'graph_data').get_text())
    with open(f'{grp1_path}/{output_file}', 'a', encoding='utf-8') as f:
        f.write(graph_raw + '\n')
    time.sleep(random.uniform(0.2, 0.5))


##
# w_date = datetime.datetime.now().strftime("%Y%m%d")
keyword_w_date = '20210201'
output_w_date = '20210215'
grp1_path = './result_data/grp_1st'
output_file = f'keyword_crawling_{output_w_date}.txt'


def naver_crawl2(work_key_cnt, output_file):
    src_str = ''
    cnt = 0
    basedate = '20170102'
    for i in range(work_key_cnt, work_key_cnt + 5):
        # key_grp=rl[i].decode("utf-8").strip().split(',')
        # grp=key_grp[0]
        # key=str.lower(key_grp[1])
        key = rl[i]
        src_str += key + '__SZLIG__' + key + '__OUML__'
        # 키워드 리스트의 마지막 항목 이거나 그룹핑 최대 횟수에 도달할경우 request처리
        if i == len(rl) - 1 or cnt == 4:
            # print(src_str)
            # req_cnt += 1
            cnt = -1
            src_str = src_str[:-8]
            # print(src_str)
            get_data(src_str, basedate, output_file)

            # sys.stdout.write(f'\r | {work_key_cnt} / {total_key_cnt} |  /  |     |{src_str}                                                                    ')
            # sys.stdout.flush()
            # src_str=''
        work_key_cnt += 1
        cnt += 1
    return work_key_cnt, total_key_cnt, src_str


df = pd.read_csv(f'./keyword_list/{keyword_w_date}_keyword_list.txt')
rl = df['keyword'].to_list()
grp1_path = './result_data/grp_1st'
total_key_cnt = len(rl)
retry_count = 100
loop_count = 100
work_key_cnt = 78315
src_str = ''
print(datetime.datetime.now())
# 9118
# req_cnt = 0

# while loop_count > 0 and retry_count > 0 and work_key_cnt < 453355 :
while work_key_cnt < 150010:
    try:

        # print(work_key_cnt, req_cnt)
        work_key_cnt, total_key_cnt, src_str = naver_crawl2(work_key_cnt, output_file)
        # work_key_cnt = work_key_cnt + (req_cnt *5) +1
        sys.stdout.write(
            f'\r | {work_key_cnt} / {total_key_cnt} |  /  |     |{src_str}                                                                    ')
        sys.stdout.flush()

        loop_count -= 1

    except Exception:
        # print(work_key_cnt,crawl_cnt)
        # tmp_df=pd.read_csv(f'{grp1_path}/{output_file}',engine='c', error_bad_lines=False)
        # tmp_num = len(tmp_df)
        # work_key_cnt = work_key_cnt + (req_cnt *5) + 1
        print("Failed! Retrying...", work_key_cnt, datetime.datetime.now())
        retry_count -= 1
        loop_count -= 1
        time.sleep(120)
        continue
print(datetime.datetime.now())