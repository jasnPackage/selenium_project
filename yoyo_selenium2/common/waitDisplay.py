#coding:utf-8
'''
显示等待元素方法封装
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException

def waitDisplayElement(driver,locator,timeout=10):
    '''定位方法封装成函数'''
    # lambda判断元素是否存在
    # element = WebDriverWait(driver, timeout,1).until(lambda x : x.find_element(*locator))

    # presence_of_element_located判断元素是否存在

    locator_n = ("css",locator)
    try:
        WebDriverWait(driver, timeout, 1).until(EC.presence_of_element_located(locator_n))
    except (TimeoutException,NoSuchElementException):
        print("元素没有定位到%s" % str(locator_n))
