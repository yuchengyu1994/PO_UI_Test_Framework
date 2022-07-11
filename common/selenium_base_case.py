import unittest
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import read_config
from common.log_utils import log_pri

class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        log_pri.info('-------------测试类开始执行-----------')
        cls.url = read_config.get_url

    def setUp(self) -> None:
        log_pri.info('-------------测试方法开始执行------------')
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_maxwindow()
        self.base_page.implicitly_wait()
        self.base_page.open_url(self.url)

    def tearDown(self) -> None:
        log_pri.info('-------------测试方法执行完毕------------')
        self.base_page.quit_driver()

    @classmethod
    def tearDownClass(cls) -> None:
        log_pri.info('-------------测试类执行完毕-----------')
