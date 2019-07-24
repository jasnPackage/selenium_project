#coding:utf-8
'''
这里写了一个163邮箱登录页面的pageobject
'''
from PageElement.readYaml import parseyaml
from common.highLight import highLightElement
from common.waitDisplay import waitDisplayElement

class Mail163_login_page():
    '''
    163邮箱登录page类
    '''

    getElement = parseyaml()

    psw_mail = getElement["mail163"]["psw_mail"]["value"]
    mail_login = getElement["mail163"]["mail_login"]["value"]
    psw_login = getElement["mail163"]["psw_login"]["value"]
    login_frame = getElement["mail163"]["login_frame"]["value"]



    def __init__(self,driver):
        self.driver = driver


    def click_psw_mail(self,type_a="css"):
        '''点击切换到账号密码登录'''

        # 调用显示等待元素的函数
        waitDisplayElement(self.driver,self.psw_mail)

        ele1 = self.driver.find_element(type_a,self.psw_mail)

        # 调用高亮显示的封装函数
        highLightElement(self.driver, ele1)

        ele1.click()


    def input_mail(self,mail_account,type_a="css"):
        '''输入邮箱账号'''

        # 调用显示等待元素的函数
        waitDisplayElement(self.driver, self.mail_login)

        ele2 = self.driver.find_element(type_a,self.mail_login)

        # 调用高亮显示的封装函数
        highLightElement(self.driver, ele2)

        ele2.send_keys(mail_account)


    def input_psw(self,mail_psw,type_a="css"):
        '''输入邮箱密码'''

        # 调用显示等待元素的函数
        waitDisplayElement(self.driver, self.psw_login)

        ele3 = self.driver.find_element(type_a,self.psw_login)

        # 调用高亮显示的封装函数
        highLightElement(self.driver, ele3)

        ele3.send_keys(mail_psw)


    def switch_loginframe(self,type_a="css"):
        '''切换到账号密码输入框的frame'''
        loginframe = self.driver.find_element(type_a,self.login_frame)
        self.driver.switch_to.frame(loginframe)
