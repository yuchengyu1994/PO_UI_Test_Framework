import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import log_pri

current_path=os.path.dirname(__file__)
driver_path=os.path.join(current_path,'../webdriver/chromedriver.exe')
# logutils=LogUtils()
class LoginPage:
    def __init__(self):
        # self.logutils=log_pri
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1/zentao/user-login.html?tid=mdjkhgvq')
        self.username_inputbox = self.driver.find_element(By.XPATH,'//input[@name="account"]')  #属性 --> 页面上的控件
        self.password_inputbox = self.driver.find_element(By.XPATH,'//input[@name="password"]')
        self.login_button = self.driver.find_element(By.XPATH,'//button[@class="btn btn-primary" and @type="submit"]')
        self.keeplogin_checkbox = self.driver.find_element(By.XPATH,'//input[@name="keepLogin[]"]')
        self.forgetpassword_link = self.driver.find_element(By.XPATH,'//a[starts-with(@href,"/zentao/user-reset.html?tid=md")]')

    def input_username(self,username):    #方法--> 控件的操作
        self.username_inputbox.send_keys(username)
        log_pri.info('用户名输入框输入:'+str(username))

    def input_password(self,password):
        self.password_inputbox.send_keys(password)
        log_pri.info('密码输入框输入:'+str(password))

    def click_login(self):
        self.login_button.click()
        log_pri.info('点击登录按钮')

    def clik_forgetpassword_link(self):
        self.forgetpassword_link.click()
        log_pri.info('点击忘记密码')

if __name__ == '__main__':
    login_page=LoginPage()
    login_page.input_username('test01')
    login_page.input_password('Aa2128199')
    login_page.click_login()
    # login_page.clik_forgetpassword_link()