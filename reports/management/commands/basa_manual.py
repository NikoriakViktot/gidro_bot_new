import datetime
import base64
import time
from selenium import webdriver
import os
from dotenv import load_dotenv

def get_auth_header(user, password):
    b64 = "Basic " + base64.b64encode('{}:{}'.format(user, password).encode('utf-8')).decode('utf-8')
    return {"Authorization": b64}



driver = webdriver.Chrome('E:/ВІТЯ/gidro_bot/chromedriver.exe')

driver.execute_cdp_cmd("Network.enable", {})
load_dotenv()
driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": get_auth_header(os.getenv('user'), os.getenv("password"))})


driver.get('http://gcst.meteo.gov.ua/armua/sino/index.phtml')

time.sleep(5)

submenu =driver.find_element_by_class_name('submenu').find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[10]').click()

time.sleep(5)
spusok_indexiv = '42256 42130 42249 42136 42137 42140 42148 42191 42187 42194 42198 42202 '

forma_index = driver.find_element_by_class_name('t1').send_keys(spusok_indexiv)

time.sleep(5)

data_time = driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[2]/td[1]/table/tbody/tr[3]/td/font/input[2]').clear()

time.sleep(1)

data_time_send = driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[2]/td[1]/table/tbody/tr[3]/td/font/input[2]').send_keys(datetime.date.today().strftime("%Y-%m-%d")+ ' ' + '09:00:36')

time.sleep(5)

input_post = driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[1]/td/input[2]').click()

time.sleep(5)

data_file = datetime.date.today().strftime("%Y-%m-%d")
file_object = open(f'E:/ВІТЯ/gidro_bot/data_html/{data_file}.html', "w", encoding=('koi8-u'))
html = driver.page_source
file_object.write(html)
file_object.close()
driver.close()
driver.quit()
