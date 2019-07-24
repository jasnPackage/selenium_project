import unittest
from selenium import webdriver
from page_object.login_page import Login_Page
from common.screen import Screen

login_url = "https://passport.cnblogs.com/user/signin"


class Test_login(unittest.TestCase):


    u'''登录页面的case'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login = Login_Page(self.driver)
        self.login.open(login_url)

    def tearDown(self):
        self.login.quit()

    @unittest.skip(u"无条件跳过此用例")
    # @Screen(driver)
    def test_login(self):
        '''博客登录测试'''
        # 调用登录类里面的login方法
        self.login.login("jsan","!kidd100cr")

        nickname_locator = ("css selector","div#header_user_right11>a:nth-child(2)")
        blog_text = self.login.get_text(nickname_locator)

        print('blog_text：%s'%blog_text)
        self.assertEqual(blog_text,"悠然现南山")





