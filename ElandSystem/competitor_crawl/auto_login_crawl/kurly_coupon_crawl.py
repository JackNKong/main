from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

###마켓컬리 쿠폰조회하기

driver = webdriver.Chrome(r'D:/Python/chromedriver.exe')
url = 'https://www.kurly.com/shop/member/login.php?return_url=/shop/event/kurlyEvent.php?gclid=Cj0KCQiAvbiBBhD-ARIsAGM48bxT1bXh863pFuBqCnfUyqTZaPWUHphxRR2mLtDLxm1RKTm_7_4HYawaAug_EALw_wcB&htmid=event/join/join_210203&utm_campaign=joinpage&utm_content=pc_brand&utm_medium=2102&utm_source=1055&utm_term=%EB%A7%88%EC%BC%93%EC%BB%AC%EB%A6%AC'
driver.get(url)
datas = []
id_pass_list = [('####', '####')]
for id_, password in id_pass_list:
    ###로그인
    tmp_dic = {}
    driver.find_element_by_name('m_id').send_keys(id_)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element(By.CLASS_NAME, 'btn_type1').click()
    driver.find_element(By.CLASS_NAME, 'name').click()
    driver.find_element(By.XPATH, '//*[@id="myPageTop"]/div/div/ul/li[2]/div/a').click()
    item_list = driver.find_elements_by_xpath('//*[@id="content"]/div[4]/div[2]/table/tbody/tr')
    for item in item_list:
        # print(item.text)
        td_list = item.find_elements_by_tag_name('td')
        tmp_dic['coupon_name'] = td_list[0].text
        tmp_dic['coupon_function'] = td_list[1].text
        tmp_dic['coupon_rate'] = td_list[2].text
        tmp_dic['coupon_duedate'] = td_list[3].text
        tmp_dic['coupon_use_TF'] = td_list[4].text
        datas.append(tmp_dic)

        # for td in td_list :
        #     = td.text
        # tmp['coupon_name'] = item.find_element(By.CLASS_NAME, 'name').text

    # //*[@id="content"]/div[4]/div[2]/table/tbody/tr[1]/td[1]/text()
    # //*[@id="content"]/div[4]/div[2]/table/tbody/tr[1]/td[1]/text()
    # //*[@id="content"]/div[4]/div[2]/table/tbody/tr[2]/td[1]/text()
    # driver.find_element_by_class('btn_type1').clilck()

df = pd.DataFrame(datas)
