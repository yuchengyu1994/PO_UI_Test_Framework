import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common.config_utils import read_config

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, '..', read_config.driver_path)


class Browser:
    def __init__(self, driver_name=read_config.driver_name, driver_path=driver_path):
        self.__driver_path = driver_path
        self.__driver_name = driver_name

    def get_driver(self):
        if self.__driver_name.lower()=='chrome':
            return self.__get_chrome_driver()
        elif self.__driver_name.lower()=='firefox':
            return self.__get_firefox_driver()

    def __get_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
        chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制提示
        chrome_options.add_experimental_option("prefs", {"credentials_enable_service": False,
                                                        "profile.password_manager_enabled": False})
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 取消chrome受自动控制提示
        chrome_driver_path = os.path.join(self.__driver_path, 'chromedriver.exe')
        driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver_path)
        return driver

    def __get_firefox_driver(self):
        firefox_driver_path = os.path.join(self.__driver_path, 'geckodriver.exe')
        driver = webdriver.Firefox(executable_path=firefox_driver_path)
        return driver


if __name__ == '__main__':
    # Browser().get_chrome_driver()
    Browser().get_driver()

