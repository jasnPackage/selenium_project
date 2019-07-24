import unittest,time
from selenium import webdriver
from page_object.maillogin_page import Mail163_login_page


maillogin_url = "https://mail.163.com/"

@unittest.skip(u"无条件跳过此用例")
class Test_maillogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = Mail163_login_page(self.driver)
        self.driver.get(maillogin_url)


    def tearDown(self):
        self.driver.quit()


    def test_maillogin(self):
        '''163邮箱登录测试'''

        self.page.click_psw_mail()

        self.page.switch_loginframe()
        self.page.input_mail("amazing")
        self.page.input_psw("123456678")



