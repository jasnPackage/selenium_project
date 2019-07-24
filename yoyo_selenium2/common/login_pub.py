#coding:utf-8
'''
这里写了一个登录博客园的类，登录博客园方法
'''
import time,os
from selenium.webdriver.support.wait import WebDriverWait
from common.base import Base



cur_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
pic_path = os.path.join(cur_path,"pic") #图片文件夹

print("\033[31mpic path:\033[0m%s"%pic_path)

class Login_Blog():
    '''登录类封装'''
    def __init__(self,driver):
        '''初始化driver参数'''
        self.driver = driver
        self.driver_n = Base(self.driver)


    def input_user(self,username):
        '''输入用户名'''

        username_locator = ("id","LoginName")
        self.driver_n.send_keys(username_locator,username)

        # WebDriverWait(self.driver,10).until(lambda x: x.find_element("id","LoginNamexx")).clear()
        # WebDriverWait(self.driver, 10).until(lambda x: x.find_element("id", "LoginNamexx")).send_keys(username)

    def input_psw(self,psw):
        '''输入密码'''

        password_locator = ("id","Password")
        self.driver_n.send_keys(password_locator,psw)


        # self.driver.find_element_by_id("Password").clear()
        # self.driver.find_element_by_id("Password").send_keys(psw)

    def click_button(self):
        '''点击登录按钮'''

        loginbutton_locator = ("id","submitBtn")
        self.driver_n.click(loginbutton_locator)

        # self.driver.find_element_by_id("submitBtn").click()


    def login(self,username,psw):
        '''登录公共方法'''

        try:
            self.input_user(username)
            self.input_psw(psw)
            self.click_button()
        except Exception as msg:
            print(u"异常原因%s"%msg)
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            t = self.driver.get_screenshot_as_file(os.path.join(pic_path,'%s.jpg' % nowTime))
            print(u"截图结果：%s"%t)