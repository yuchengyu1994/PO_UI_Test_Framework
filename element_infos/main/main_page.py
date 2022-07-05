from element_infos.login.login_page import LoginPage
from selenium.webdriver.common.by import By
from common.log_utils import log_pri
from common.base_page import BasePage

# logutils=LogUtils()
class MainPage(BasePage):
    def __init__(self,driver):
        super(MainPage, self).__init__(driver)
        # self.logutils=logutils
        login_page = LoginPage()
        login_page.input_username('test01')
        login_page.input_password('Aa2128199')
        login_page.click_login()
        self.driver=login_page.driver
        self.myzone_menu=self.driver.find_element(By.XPATH,'//i[@class="icon icon-menu-my"]')
        self.product_menu=self.driver.find_element(By.XPATH,'//i[@class="icon icon-product"]')
        # self.driver.switch_to.frame('appIframe-my')
        # self.username_showspan =self.driver.find_element(By.XPATH,'//a[@class="dropdown-toggle"]/div[@class="avatar has-text avatar-circle"]/span[@class="text text-len-1"]')

    def goto_myzone(self): #进入我的地盘
        self.myzone_menu.click()
        log_pri.info('点击进入地盘页面')

    def goto_product(self): #进入产品页面
        self.product_menu.click()
        log_pri.info('点击进入产品页面')

    # def get_username(self): #获取用户的简写
    #     return self.username_showspan.text


if __name__=='__main__':
    mainpage=MainPage()
    mainpage.goto_product()
    # mainpage.switch_to_frame('appIframe-my')
    # a=mainpage.get_username()
    # print(a)