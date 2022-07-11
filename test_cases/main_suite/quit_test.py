import unittest
from common.browser import Browser
from common.base_page import BasePage
from actions.login_action import LoginAction
from common.config_utils import read_config
from actions.quit_action import QuitAction
from common.selenium_base_case import SeleniumBaseCase


class QuitTest(SeleniumBaseCase):
    def test_quit(self):
        login_action=LoginAction(self.base_page.driver)
        main_page=login_action.default_login()
        quit_action=QuitAction(main_page.driver)
        quit_action.quit_user_action()
        self.assertEqual(main_page.get_title(),'用户登录 - 禅道','test_quit执行失败')

if __name__ == '__main__':
    unittest.main(verbosity=2)
