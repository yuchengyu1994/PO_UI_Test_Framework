import unittest
from actions.login_action import LoginAction
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils

class LoginTest(SeleniumBaseCase):

    test_data = TestDataUtils('login_suite', 'LoginTest').convert_exceldata_to_testdata()
    def setUp(self) -> None:         ###在二次封装号unittest后，如果setup 需要自定义，可以如左边这样做
        super().setUp()

    @unittest.skipIf(test_data['test_login_success']['isnot'],'')
    def test_login_success(self):
        test_function_data = self.test_data['test_login_success']
        self._testMethodDoc = test_function_data['test_name']
        login_action=LoginAction(self.base_page.driver)
        main_page=login_action.login_success(test_function_data['test_parameter']['username']\
                                             ,test_function_data['test_parameter']['password'])
        self.assertEqual(main_page.get_zone(),test_function_data['excepted_result'],'测试用例test_login_success执行失败')

    def test_login_fail(self):
        test_function_data=self.test_data['test_login_fail']
        login_action=LoginAction(self.base_page.driver)
        actual_result=login_action.login_fail(test_function_data['test_parameter']['username'],\
                                              test_function_data['test_parameter']['password'])
        self.assertEqual(actual_result,test_function_data['excepted_result'],'测试用例test_login_success执行失败')


if __name__=='__main__':
    unittest.main(verbosity=2)
