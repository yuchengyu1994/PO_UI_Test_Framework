import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import log_pri
from common.base_page import BasePage
from common.element_data_utils import ElementDataUtils
from common.browser import Browser


class LoginPage(BasePage):
    def __init__(self,driver):
        super(LoginPage, self).__init__(driver)
        element_info=ElementDataUtils('login','login_page').get_element_info()
        self.username_inputbox = element_info['username_inputbox']
        self.password_inputbox = element_info['password_inputbox']
        self.login_button = element_info['login_button']
        # self.bug_link = ElementDataUtils('login','login_page').get_element_info('bug_link')


    def input_username(self, username):  # 方法--> 控件的操作
        # self.driver.find_element(By.XPATH,self.username_inputbox['locator_value'])
        # log_pri.info('用户名输入框输入:'+str(username))
        super().input(self.username_inputbox, username)

    def input_password(self, password):
        # self.password_inputbox.send_keys(password)
        # log_pri.info('密码输入框输入:'+str(password))
        super().input(self.password_inputbox, password)

    def pri(self):
        print(self.bug_link)

    def click_buglink(self, bug_title):
        self.bug_link['locator_value']=self.bug_link['locator_value']%bug_title
        self.bug_link['element_name']=self.bug_link['element_name']%bug_title
        self.click(self.bug_link)


    def click_login(self):
        # self.login_button.click()
        # log_pri.info('点击登录按钮')
        super().click(self.login_button)

    # def clik_forgetpassword_link(self):
    #     self.forgetpassword_link.click()
    #     log_pri.info('点击忘记密码')


if __name__ == '__main__':
    driver= Browser().get_driver()
    login_page = LoginPage(driver)
    login_page.set_maxwindow()
    login_page.open_url('http://127.0.0.1/zentao/user-login.html?tid=mdjkhgvq')
    login_page.input_username('test01')
    login_page.input_password('Aa2128199')
    login_page.click_login()


    # print(login_page.get_element_info('username_inputbox'))
    # login_page.clik_forgetpassword_link()
