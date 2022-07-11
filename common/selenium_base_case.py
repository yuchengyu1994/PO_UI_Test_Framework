import unittest
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import read_config

class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = read_config.get_url

    def setUp(self) -> None:
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_maxwindow()
        self.base_page.implicitly_wait()
        self.base_page.open_url(self.url)

    def tearDown(self) -> None:
        self.base_page.quit_driver()