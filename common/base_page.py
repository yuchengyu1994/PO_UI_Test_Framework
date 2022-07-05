import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.log_utils import log_pri
from common.config_utils import read_config


class BasePage:
    def __init__(self, driver):
        self.driver =  driver # webdriver.Chrome()

    # 浏览器的操作封装
    def open_url(self, url):
        self.driver.get(url)
        log_pri.info('打开url地址%s' % url)

    def set_maxwindow(self):
        self.driver.maximize_window()
        log_pri.info('设置浏览器最大化')

    def set_minwindow(self):
        self.driver.minimize_window()
        log_pri.info('设置浏览器最小化')

    def refresh(self):
        self.driver.refresh()
        log_pri.info('浏览器进行刷新')

    def get_title(self):
        value = self.driver.title
        log_pri.info('获取网页标题，标题是%s'%value)
        return value

    def switch_to(self,element_info):
        self.implicitly_wait(3)
        element=self.find_element(element_info)
        self.driver.switch_to.frame(element)
        log_pri.info('跳转到页面%s'%element_info['element_name'])

    def find_element(self,element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_time = element_info['timeout']
        if locator_type_name=='id':
            locator_type = By.id
        elif locator_type_name== 'class':
            locator_type = By.id
        elif locator_type_name== 'xpath':
            locator_type = By.XPATH
        # element = WebDriverWait(self.driver,locator_time)\
        #     .until(lambda x:x.find_element(locator_type,locator_value_info))
        element = WebDriverWait(self.driver, locator_time).\
            until(EC.presence_of_element_located((locator_type,locator_value_info)))
        log_pri.info('%s元素识别成功'%element_info['element_name'])
        return element

    def click(self,element_info):
        element=self.find_element(element_info)
        element.click()
        log_pri.info('对%s进行了点击'%element_info['element_name'])

    def input(self,element_info,content):
        self.find_element(element_info).send_keys(content)
        log_pri.info(element_info['element_name']+'输入:'+content)

    def scrolltop_bynumber(self,number):
        js_str='document.body.scrollTop=%d'%number
        self.driver.execute_script(js_str)
        log_pri.info('对浏览器进行移动%d'%number)

    def scrolltop_element(self,element_info):
        element=self.find_element(element_info)
        self.driver.execute_script('arguments[0].scrollIntoView();',element)
        log_pri.info('对浏览器移动到元素%s'%element_info['element_name'])

    def remove_element_attribute(self,element_info,attribute_name):
        element=self.find_element(element_info)
        self.driver.execute_script('arguments[0].removeAttribute("%s");'%attribute_name,element)
        log_pri.info('删除元素%s的属性%s'%(element_info['element_name'],attribute_name))

    def modify_element_attribute(self,element_info,attribute_name,attribute_value):
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].setAttribute("%s","%s");'%(attribute_name,attribute_value))
        log_pri.info('替换元素%s的属性%s，改为%s' % (element_info['element_name'], attribute_name,attribute_value))

    def wait(self,seconds=read_config.time_out):
        time.sleep(seconds)
        log_pri.info('固定等待%s秒'%seconds)

    def implicitly_wait(self,seconds=read_config.time_out):
        self.driver.implicitly_wait(seconds)
        log_pri.info('设置隐式等待%s秒'%seconds)






