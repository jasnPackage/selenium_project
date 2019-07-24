#coding:utf-8
'''
这里写了一个百度搜索页的pageobject
'''
from PageElement.readYaml import parseyaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.highLight import highLightElement
from common.waitDisplay import waitDisplayElement



class Baidu_page():
    '''
    百度搜索page类
    '''

    getElement = parseyaml()



    search_box = getElement["baiduPage"]["search_box"]["value"]
    baidu_button = getElement["baiduPage"]["baidu_button"]["value"]
    search_result = getElement["baiduPage"]["search_result"]["value"]





    def __init__(self,driver):
        self.driver = driver

    def input_search(self,keyword,type_a="css"):
        '''输入搜索关键词'''

        # 调用显示等待元素的函数
        waitDisplayElement(self.driver, self.search_box)

        ele1 = self.driver.find_element(type_a,self.search_box)

        # 调用高亮显示的封装函数
        highLightElement(self.driver, ele1)

        ele1.send_keys(keyword)




    def click_baidubutton(self,type_a="css"):
        '''点击百度一下按钮'''
        # 调用显示等待元素的函数
        waitDisplayElement(self.driver, self.baidu_button)

        ele2 = self.driver.find_element(type_a, self.baidu_button)

        # 调用高亮显示的封装函数
        highLightElement(self.driver, ele2)

        ele2.click()


    def verification_result(self,type_a="css"):
        '''用例结果验证'''
        # WebDriverWait(self.driver,10).until(lambda x: x.find_element("css selector",self.search_result))
        # results = self.driver.find_elements("css selector", self.search_result)


        results = WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((type_a,self.search_result)))
        print(results)

        nanjing_baike = results[0].text
        return nanjing_baike

