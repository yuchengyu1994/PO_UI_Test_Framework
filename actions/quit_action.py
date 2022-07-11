from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.config_utils import read_config

class QuitAction:
    def __init__(self,driver):
        self.__main_page = MainPage(driver)

    def quit_user_action(self):
        self.__main_page.switch_to_appIframe()
        self.__main_page.click_user_menu()
        self.__main_page.click_quit_button()
        return LoginPage(self.__main_page.driver)
