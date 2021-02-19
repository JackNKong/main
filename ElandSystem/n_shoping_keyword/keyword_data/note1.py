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
from sklearn.cluster import KMeans
import matplotlib.pyplot  as plt
###db가져오는거 생략
k = 15
# create model and prediction
model = KMeans(n_clusters=k,algorithm='auto')
k_df = df1[['avg']]
print(model.fit(k_df))
predict = pd.DataFrame(model.predict(k_df))
predict.columns=['predict']
final_df = pd.DataFrame(np.hstack((df1, predict)))
print(len(final_df))
final_df.head(10)

final_df=final_df.rename(columns={0:'keyword',1:'min',2:'max',3:'avg',4:'scale_std',5:'cluster_id'})
final_df=final_df.sort_values(by=['cluster_id','scale_std'],ascending=False)
final_df= pd.merge(final_df,df2, on= 'keyword', how ='left')
final_df = final_df.fillna(value = {'scale':0})
final_df.head(10)
### 201701월 정량 스케일

##기준일 scale 0으로 2그룹 분리하기
final_df=final_df.drop_duplicates(subset=['keyword'])
scale0_df = final_df[final_df['scale']==0]
scale1_df = final_df[final_df['scale']>0]
scale1_idx=[i for i in range(0,1000000) if i%5 in [0]]
scale1_idx=scale1_idx[:len(scale1_df)]
scale0_idx=[i for i in range(0,1000000) if i%5 in [1,2,3,4]]
scale0_idx=scale0_idx[:len(scale0_df)]
scale1_df.index=scale1_idx
scale0_df.index=scale0_idx
fin_df= pd.concat([scale1_df,scale0_df])
fin_df=fin_df.rename(columns ={'scale':'20170102_scale'})
fin_df=fin_df.sort_index()
print(fin_df.head(10))
print(len(fin_df), )

##조 이름 정하고 조별 scale 0개수 확인하기
#fin_df=fin_df.drop_duplicates(subset=['keyword'])
fin_df=fin_df.reset_index(drop=True)
#fin_df=fin_df.sort_index()
fin_df['group_id'] = fin_df.index//5 +1
##group_id별로 0아닌거 개수 확인하기
group_id=pd.DataFrame()
fin_df2 =fin_df
fin_df2['tmp_num'] = fin_df2.apply(lambda x: 1 if (x['20170102_scale'] > 0) else 0,axis = 1 )
group_id=fin_df2.groupby(by='group_id')['tmp_num'].sum()
group_id.unique()