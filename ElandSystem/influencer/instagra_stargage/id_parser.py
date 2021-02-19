import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import random
import traceback,sys


df = pd.read_csv('stargage_influencer.txt')
url_list = df['stargage_url'].to_list()
id_list = df['influencer_id'].to_list()
zip_list = list(zip(id_list,url_list))

datas = []

for num, zip_ in enumerate(zip_list[:1000]):
    try:
        tmp_dic = {}
        tmp_dic['influencer_id'] = zip_[0]
        res = requests.get(zip_[1], headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        tmp_dic['avg_likes'] = soup.find('div', class_='card avg-likes').find('div',
                                                                              class_='h3 m-0 text-number pl-4 ml-3').text
        tmp_dic['avg-comments'] = soup.find('div', class_='card avg-comments').find('div',
                                                                                    class_='h3 m-0 text-number pl-4 ml-3').text
        tmp_dic['posts'] = soup.find('div', class_='card posts').find('div', class_='h3 m-0 text-number pl-4 ml-3').text
        tmp_dic['global-rank'] = soup.find('div', class_='card global-rank').find('div',
                                                                                  class_='h3 m-0 text-number pl-4 ml-3').text
        tmp_dic['country-rank'] = soup.find('div', class_='card country-rank').find('div',
                                                                                    class_='h3 m-0 text-number pl-4 ml-3').text
        tmp_dic['category-rank'] = soup.find('div', class_='card category-rank').find('div',
                                                                                      class_='h3 m-0 text-number pl-4 ml-3').text
        # tmp_list = soup.find_all('ul', class_= 'list-group')
        if soup.find('ul', class_='list-group'):
            tmp_list = soup.find('ul', class_='list-group').find_all('span', class_='flex-fill ml-3')
            tmp_list = [tmp.text for tmp in tmp_list]
            tmp_list2 = soup.find('ul', class_='list-group').find_all('span', class_='font-weight-bold text-nowrap')
            tmp_list2 = [tmp.text for tmp in tmp_list2]
            audience_interest = list(zip(tmp_list, tmp_list2))
            tmp_dic['audience_interest'] = audience_interest
        else:
            pass

        if soup.find('div', class_='card-columns'):
            recent_post_list = soup.find('div', class_='card-columns').find_all('a')
            for i, post in enumerate(recent_post_list):
                # tmp_dic['recent_post_url'+str(i)] = post['href']
                # url 좋아오 조회수등 가능
                post_text = post.find('p').text.split("#")
                if len(post_text) == 2:
                    tmp_dic['recent_post_hash' + str(i)] = [post_text[1]]
                elif len(post_text) > 2:
                    tmp_dic['recent_post_hash' + str(i)] = [post_text[1]] + post_text[2:]
                else:
                    tmp_dic['recent_post_hash' + str(i)] = None
        else:
            pass
        # tmp_dic['recent_post'] = soup.find('div',class_='card-columns')

        datas.append(tmp_dic)
        sys.stdout.write(f'\r{num}_{zip_}')
        sys.stdout.flush()

        # print(zip_)
    except:
        traceback.print_exc()
    time.sleep(random.uniform(0.5, 1))

df2= pd.DataFrame(datas)
fin_df = pd.merge(df,df2, on = 'influencer_id',how='left')