import json
import requests
from bs4 import BeautifulSoup as bs
import datetime
import time, random

w_date = datetime.datetime.now().strftime('%Y%m%d')

cate_dict = {'SFMA41A07': '여성_아우터', 'SFMA41A21': '여성_재킷/베스트', 'SFMA41A01': '여성_티셔츠', 'SFMA41A02': '여성_셔츠/블라우스',
             'SFMA41A03': '여성_니트', 'SFMA41A06': '여성_원피스', 'SFMA41A04': '여성_팬츠', 'SFMA41A05': '여성_스커트', 'SFMA41A09': '여성_비치웨어',
             'SFMA42A03': '남성_니트','SFMA42A04' : '남성_팬츠','SFMA42A06':'남성_정장','SFMA42A09':'남성_가방/지갑','SFMA42A11' :'남성_패션잡화',
             'SFMA42A10': '남성_신발','SFMA42A08': '남성_비치웨어','SFMA42A07':'남성_언더웨어'
            } ### 여성 41 남성 42
url_main = 'https://www.ssfshop.com'
jl_f = open(f'./result/SSFMALL_Prod_Data_%s.jl' % (w_date) , 'w', encoding='utf-8')  #json file
#txt_f = open(f'./result/test%s.txt' % (w_date), 'w', encoding='utf-8')  #text file
k=0
for m_cate_cd in list(cate_dict.keys())[k:]:
    l_cate_nm = cate_dict[m_cate_cd].split('_')[0]
    m_cate_nm = cate_dict[m_cate_cd].split('_')[1]  # 중분류명    
    url = f'https://www.ssfshop.com/selectProductList?dspCtgryNo={m_cate_cd}'
    #url = f'https://www.ssfshop.com/WOMEN/list?dspCtgryNo={cate}'
    r = requests.get(url)
    soup = bs(r.content,'lxml')
    li_list = soup.find('ul',id = 'dspGood').find_all('li')
    product_data = {}
    rank_num = 0
    for prod in li_list:
        #prd_nm = li.find('span',class_='name').get_text().strip()    
        #print(prd_nm)
        rank_num += 1
        data = prod.find('div', class_='info')  # 상품 데이터 영역
        price = data.find('span', class_='price').get_text().split('\n')
        img_url = prod.img['src']
        img_url2 = prod.find('img')['src']
        prod_cd = img_url.split('/')[-1].split('_')[0]
        prod_url = '%s/Beanpole-Sport/%s/good?dspCtgryNo=%s' % (url_main, prod_cd, m_cate_cd)
        brand_nm = data.find('span', class_='brand').get_text(strip=True)
        prod_nm = data.find('span', class_='name').get_text(strip=True)
            # 가격 영역
        if len(price) < 5:  # 할인 전 가격 없음
            s_price = price[2].strip().replace(',', '').replace('원', '')
            o_price = s_price
        else:  # 할인 전 가격 있음
            s_price = price[2].strip().replace(',', '').replace('원', '')
            o_price = price[5].strip().replace(',', '').replace('원', '')
        dc_rate = (int(o_price)-int(s_price))/int(o_price)

        like_cnt = data.find('span', class_='heart').get_text().replace(',', '').replace('♡', '')
        if like_cnt == '': like_cnt = 0
        rev_cnt = data.find('span', class_='review').get_text().replace(',', '').replace('리뷰', '')
        if rev_cnt == '': rev_cnt = 0
        
        product_data['w_date'] = w_date
        product_data['comp_cd'] = "SSFSHOP"
        product_data['comp_nm'] = "SSF샵"
        product_data['l_cate_cd']=str(m_cate_cd[:6])
        product_data['l_cate_nm']=cate_dict[m_cate_cd].split('_')[0] +"의류"
        product_data['m_cate_cd']=str(m_cate_cd)
        product_data['m_cate_nm']=cate_dict[m_cate_cd].split('_')[1]
        product_data['img_url']=prod.img['src']
        product_data['prod_cd'] =str(img_url.split('/')[-1].split('_')[0])
        #product_data['prod_url'] = '%s/Beanpole-Sport/%s/good?dspCtgryNo=%s' % (url_main, prod_cd, m_cate_cd)
        product_data['prod_url'] = '%s/Beanpole-Sport/%s/good' % (url_main, prod_cd)
        product_data['brand_nm'] = data.find('span', class_='brand').get_text(strip=True)
        product_data['prod_nm'] = data.find('span', class_='name').get_text(strip=True).strip()
        if len(price) < 5: 
            product_data['s_price'] = price[2].strip().replace(',', '').replace('원', '')
            product_data['o_price'] = s_price
        else : 
            product_data['s_price'] = price[2].strip().replace(',', '').replace('원', '')
            product_data['o_price'] = price[5].strip().replace(',', '').replace('원', '')
        
        product_data['rank_num'] = rank_num
        product_data['dc_rate'] = (int(o_price)-int(s_price))/int(o_price)
        product_data['like_cnt'] = data.find('span', class_='heart').get_text().replace(',', '').replace('♡', '')
        if product_data['like_cnt'] == "" : product_data['like_cnt']=0
        product_data['rev_cnt'] = data.find('span', class_='review').get_text().replace(',', '').replace('리뷰', '')
        if product_data['rev_cnt'] == "" : product_data['rev_cnt']=0
        

        jl_f.write(json.dumps(product_data) + '\n')

        
    print(l_cate_nm,m_cate_nm)
    time.sleep(random.randrange(10, 15))
