import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from datetime import datetime
from datetime import date
from datetime import timedelta
import json


def findMonday(basedate):
    # base = datetime.strptime(basedate, "%Y%m%d").date()
    interval = (7 - date.weekday(basedate)) % 7
    startdate = basedate + timedelta(days=interval)
    return startdate


def day_reset():  # 메인함수

    fromdate_temp = datetime.today() - timedelta(days=7)
    fromdate = fromdate_temp.strftime("%Y%m%d")  # 지난주
    # todate = datetime.today().strftime("%Y%m%d")  # '20161128' 이번주
    startdate = findMonday(datetime.strptime(fromdate, "%Y%m%d").date()) - timedelta(days=7)
    enddate = startdate + timedelta(days=6)
    startdate = startdate.strftime("%Y%m%d")
    enddate = enddate.strftime("%Y%m%d")
    return startdate, enddate


def len_test(col1, col2):
    if len(col1) == len(col2):
        return "T"
    else:
        return "F"


def calculator_scale_1st(scale, graph_data, graph_period, start_date):
    basedate = '20191104'
    # 이날 있으면 1그룹 없으면 2그룹
    if basedate in graph_period and start_date in graph_period:
        base_idx = graph_period.index(basedate)
        idx = graph_period.index(start_date)
        return scale * graph_data[idx] / graph_data[base_idx]
    else:
        return None


def calweek_calculator(date):  # 날짜를 넣으면 주차를 반환 (yyyymmdd)
    today_datetime = datetime.datetime.strptime(date, '%Y%m%d')  # w_date의 날짜
    today_iso = today_datetime.isoweekday()  # w_date의 요일 (월1 화2 수3 목4 금5 토6 일7)
    reference_date = today_datetime + datetime.timedelta(days=(4 - today_iso))  # 주차를 정하는 기준날짜 (목요일의 날짜)
    reference_date_str = datetime.datetime.strftime(reference_date, '%Y%m%d')  # 기준날짜의 string

    first_date = datetime.date(reference_date.year, reference_date.month, 1)  # 기준날짜 포함 월의 첫날
    mon_date_list = [first_date + datetime.timedelta(days=i) for i in
                     range(calendar.monthrange(reference_date.year, reference_date.month)[1])]  # 기준날짜 포함 월의 모든 일자 리스트
    week = [datetime.datetime.strftime(date, '%Y%m%d') for date in mon_date_list if date.isocalendar()[2] == 4].index(
        reference_date_str) + 1  # 기준날짜 포함월의 모든 목요일 중 기준날짜가 몇번째 목요일인가?
    calweek = str(reference_date.month) + '월 ' + str(week) + '주'

    return calweek


def yearmonth_calculator(date):  # 날짜를 넣으면 주차를 반환 (yyyymmdd)
    today_datetime = datetime.strptime(date, '%Y%m%d')  # w_date의 날짜
    today_iso = today_datetime.isoweekday()  # w_date의 요일 (월1 화2 수3 목4 금5 토6 일7)
    reference_date = today_datetime + timedelta(days=(4 - today_iso))  # 주차를 정하는 기준날짜 (목요일의 날짜)
    reference_date_str = datetime.strftime(reference_date, '%Y%m%d')  # 기준날짜의 string
    return reference_date.strftime("%Y%m")


def keyword_cleansing(i, json_txt):
    try:
        json_txt = json.loads(json_txt)
        return json_txt[i]
    except:
        return {'title': None, 'data': None}

###이번주 새로 수집된 데이터 불러오기 df1
#sql = 'select * from sbd.stg_sbds_new_search_cnt_week;'
#cur.execute(sql)
#result = cur.fetchall()
#df = pd.DataFrame(result)

df=pd.read_csv(f'D:/work/_jeong_jaekeun/naver/new_keyword_crawl/result_data/grp_1st/keyword_crawling2_20170102.txt',header=None, sep = "\t", error_bad_lines=False)
df33=pd.read_csv(f'D:/work/_jeong_jaekeun/naver/new_keyword_crawl/result_data/grp_1st/keyword_crawling3_20170102.txt',header=None, sep = "\t", error_bad_lines=False)
df=pd.concat([df, df33],ignore_index=True)

##5개 키워드 분리
result_df=pd.DataFrame()
for i in range(0,5) :
    #df_name = "df_"+str(i)
    tmp_df=pd.DataFrame()
    tmp_df['keyword']=df.apply(lambda x: keyword_cleansing(i,x[0])['title'],axis = 1)
    tmp_df['data']=df.apply(lambda x: keyword_cleansing(i,x[0])['data'],axis = 1)
    #tmp_df['cluster_id'] = df
    result_df=pd.concat([result_df,tmp_df])
    print(len(result_df))
result_df['cluster_id'] = result_df.index

###계산하기
###기준일자
stand_start_date = '20191104'
###뽑을 날짜
return_start_date, return_end_date = ('20201207','20201213')

date_scale = return_start_date+"_scale"
merged_df[date_scale] = merged_df.apply(lambda x: caculator_1st(x['data'],x['stand_scale'],stand_start_date,return_start_date),axis =1)

w_date = datetime.now().strftime("%Y%m%d")
merged_df['start_date']= return_start_date
merged_df['end_date']=return_end_date
merged_df['indate'] =w_date
merged_df['yearmonth'] = yearmonth_calculator(return_start_date)
merged_df.head(10)

print(return_start_date)
merged_df[return_start_date+'ratio'] = merged_df.apply(lambda x: [i['value'] for i in x['data'] if i['period']==return_start_date], axis =1)

cluster_df=merged_df.groupby('group_id')['data','stand_scale'].first()
cluster_df['group_stand_ratio']=cluster_df.apply(lambda x: [i['value'] for i in x['data'] if i['period']==stand_start_date], axis =1)
cluster_df=cluster_df.rename(columns ={'stand_scale':'group_stand_scale'})

final_df=pd.DataFrame()
final_df= pd.merge(merged_df,cluster_df, how='outer',on='group_id')
final_df.head(10)

final_df[return_start_date+'ratio']= final_df.apply(lambda x: x[return_start_date+'ratio'][0] if (len(x[return_start_date+'ratio'])==1) else 0, axis =1)
final_df['group_stand_ratio']= final_df.apply(lambda x: x['group_stand_ratio'][0] if (len(x['group_stand_ratio'])==1) else 0, axis =1)
final_df[date_scale+"new"]=final_df.apply(lambda x: x['group_stand_scale']*x[return_start_date+'ratio']/x['group_stand_ratio'] if (x['group_stand_ratio']>0) else 0, axis = 1)

final_df=final_df.rename(columns = {date_scale+"new" : 'scale'})
#final_df.head(2)
final_df=final_df[['keyword','start_date','end_date','yearmonth','scale','indate']].head(20)
final_df=final_df.astype({'scale' : 'int'})

final_df.to_csv(output, header=False, index=False)
output.seek(0)
cur.copy_expert("COPY %s FROM STDIN WITH CSV" % tbl, output)
conn.commit()
cur.close()
