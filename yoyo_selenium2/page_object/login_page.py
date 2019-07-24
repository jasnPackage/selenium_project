#coding:utf-8
'''
这里写了一个登录博客园的类，登录博客园方法
'''
import time,os
from common.base import Base



cur_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
pic_path = os.path.join(cur_path,"pic") #图片文件夹

print("\033[31mpic path:\033[0m%s"%pic_path)


class Login_Page(Base):
    '''定位器，定位页面元素'''
    username_locator = ("id", "LoginName")
    password_locator = ("id", "Password")
    loginbutton_locator = ("id", "submitBtn")



    def input_user(self,username):
        '''输入用户名'''
        self.send_keys(self.username_locator,username)


    def input_psw(self,psw):
        '''输入密码'''
        self.send_keys(self.password_locator,psw)


    def click_button(self):
        '''点击登录按钮'''
        self.click(self.loginbutton_locator)


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