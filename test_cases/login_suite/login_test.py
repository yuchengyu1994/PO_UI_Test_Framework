import unittest
from common.browser import Browser
from common.base_page import BasePage
from actions.login_action import LoginAction
from common.config_utils import read_config
from common.selenium_base_case import SeleniumBaseCase

class LoginTest(SeleniumBaseCase):
    # def setUp(self) -> None:         ###在二次封装号unittest后，如果setup 需要自定义，可以如左边这样做
    #     super().setUp()
    #     print('hello')

    def test_login_success(self):
        login_action=LoginAction(self.base_page.driver)
        main_page=login_action.login_success('test01','Aa2128199')
        self.assertEqual(main_page.get_zone(),'地盘','测试用例test_login_success执行失败')

    def test_login_fail(self):
        login_action=LoginAction(self.base_page.driver)
        actual_result=login_action.login_fail('test02','123333121')
        print(actual_result)
        self.assertEqual(actual_result,'登录失败，请检查您的用户名或密码是否填写正确。','测试用例test_login_success执行失败')


if __name__=='__main__':
    unittest.main(verbosity=2)
