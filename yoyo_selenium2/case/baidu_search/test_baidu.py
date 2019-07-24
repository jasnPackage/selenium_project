import unittest,time,ddt
from selenium import webdriver
from page_object.baidu_page import Baidu_page


baidu_url = "http://www.baidu.com"

# 测试用例数据和断言assertEqual要比对的数据
testData = [{"search_word":"南京","verify_data":"南京"},
            {"search_word": "上海", "verify_data": "上海"}]


@ddt.ddt
class Test_baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = Baidu_page(self.driver)
        self.driver.get(baidu_url)


    def tearDown(self):
        self.driver.quit()


    @ddt.data(*testData)
    def test_baidu(self,data):
        '''百度搜索测试，测试数据:%s'''

        self.page.input_search(data["search_word"])
        self.page.click_baidubutton()


        vr = self.page.verification_result()
        print(vr)

        self.assertEqual(vr,data["verify_data"])


if __name__ == "__main__":
    unittest.main()