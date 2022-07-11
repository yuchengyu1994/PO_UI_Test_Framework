from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.element_data_utils import ElementDataUtils
from common.browser import Browser
from element_infos.login.login_page import LoginPage
# from actions.login import LoginAction
from common.config_utils import read_config

# logutils=LogUtils()
class MainPage(BasePage):
    def __init__(self,driver):
        super(MainPage, self).__init__(driver)
        # self.logutils=logutils
        elements=ElementDataUtils('main','main_page').get_element_info()
        self.myzone_menu=elements['myzone_menu']
        self.product_menu=elements['product_menu']
        self.exit_button=elements['exit_button']
        self.appIframe=elements['appIframe-my']
        self.user_menu=elements['user_menu']
        # self.driver.switch_to.frame('appIframe-my')
        # self.username_showspan =self.driver.find_element(By.XPATH,'//a[@class="dropdown-toggle"]/div[@class="avatar has-text avatar-circle"]/span[@class="text text-len-1"]')

    def goto_myzone(self): #进入我的地盘
        self.click(self.myzone_menu)

    def goto_product(self): #进入产品页面
        self.click(self.product_menu)

    def get_zone(self):
        self.goto_myzone()
        return self.driver.find_element(By.XPATH,'//a[@data-app="my"]/span[@class="text"]').text
    # def get_username(self): #获取用户的简写
    #     return self.username_showspan.text
    def click_quit_button(self):
        self.click(self.exit_button)

    def switch_to_appIframe(self):
        self.switch_to(self.appIframe)

    def click_user_menu(self):
        self.click(self.user_menu)




if __name__=='__main__':
    login_page=LoginPage(Browser().get_driver())
    login_page.set_maxwindow()
    login_page.open_url(read_config.get_url)
    login_page.input_username(read_config.get_username)
    login_page.input_password(read_config.get_password)
    login_page.click_login()
    main_page=MainPage(login_page.driver)
    main_page.switch_to_appIframe()
    main_page.click_user_menu()
    main_page.click_quit_button()
    # main_page.switch_to_alter()
    # main_page.goto_product()
    # mainpage.switch_to_frame('appIframe-my')
    # a=mainpage.get_username()
    # print(a)