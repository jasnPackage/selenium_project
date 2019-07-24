#coding:utf-8
from selenium import webdriver
import time

driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.find_element("id","kw").send_keys(u"南京")

driver.find_element("id","su").click()
time.sleep(2)

print(driver.title)

driver.quit()