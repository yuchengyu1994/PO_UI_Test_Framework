from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.config_utils import read_config

class LoginAction:
    def __init__(self,driver):
        self.__login_page = LoginPage(driver)

    def login_actions(self,username,password):
        self.__login_page.input_username(username)
        self.__login_page.input_password(password)
        self.__login_page.click_login()

    def login_success(self,username,password):
        self.login_actions(username,password)
        return MainPage(self.__login_page.driver)

    def default_login(self,username=read_config.get_username,password=read_config.get_password):
        return self.login_success(username,password)

    def login_fail(self,username,password):
        self.login_actions(username,password)
        return self.__login_page.get_login_fail_alert_content()

    def login_by_cookies(self):
        pass