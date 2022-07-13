import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.log_utils import log_pri
from common.config_utils import read_config
from common import HTMLTestReportCN


class BasePage:
    def __init__(self, driver):
        self.driver =  driver # webdriver.Chrome()

    # 浏览器的操作封装
    def open_url(self, url):
        try:
            self.driver.get(url)
            log_pri.info('打开url地址%s' % url)
        except Exception as e:
            log_pri.error('不能打开指定的地址%s,原因是:%s'%(url,e.__str__()))

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

    def get_url(self):
        url=self.driver.current_url
        log_pri.info('获取当前网页url，url是%s'%url)
        return url

    def get_text(self,element_info):
        log_pri.info('获取当前元素中的text')
        return self.find_element(element_info).text


    def quit_driver(self):
        self.driver.quit()
        log_pri.info('退出浏览器')


    def close_window(self):
        self.driver.close()
        log_pri.info('退出当前窗口')

    def switch_to(self,element_info):
        element=self.find_element(element_info)
        self.driver.switch_to.frame(element)
        log_pri.info('跳转到页面%s'%element_info['element_name'])
#弹窗的操作封装
    def switch_to_alert(self,action='accpet',time_out=read_config.time_out):
        WebDriverWait(self.driver,time_out).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        if action == 'accept':
            alert.accept()
        elif action == 'dismiss':
            alert.dismiss()
        return alert_text

#浏览器多窗口操作封装
    def get_current_window_handle(self): #获取当前浏览器窗口
        now_handle=self.driver.current_window_handle
        return now_handle

    def get_all_window_handle(self): #获取所有浏览器窗口的句柄
        windows_handle=self.driver.window_handles
        return windows_handle

    def swtich_to_window_by_title(self,title): #根据url 跳转到窗口
        windows_handle=self.driver.window_handles
        for window_handle in windows_handle:
            self.driver.switch_to.window(window_handle)
            if WebDriverWait(self.driver,read_config.time_out).until(EC.title_contains(title)):
                break

    def swtich_to_window_by_url(self,url):
        windows_handle=self.driver.window_handles
        for window_handle in windows_handle:
            self.driver.switch_to.window(window_handle)
            if WebDriverWait(self.driver,read_config.time_out).until(EC.url_contains(url)):
                break

    def swtich_to_window_by_handle(self,window_handle): #根据句柄，跳转到窗口
        self.driver.switch_to.window(window_handle)

    def find_element(self,element_info):
        """
        根据提供的元素数据，进行元素的查找
        :param element_info: 元素信息参数，字典类型
        :return:返回查找到的元素,element对象
        """
        try:
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
        except Exception as e:
            log_pri.error('%s元素不能识别，原因是%s'%(element_info['element_name'],e.__str__()))
            self.screenshot_as_file()
        return element

    def click(self,element_info):
        element=self.find_element(element_info)
        try:
            element.click()
            log_pri.info('对%s进行了点击'%element_info['element_name'])
        except Exception as e:
            log_pri.error('%s元素点击失败，原因是：%s'%(element_info['element_name'],e.__str__()))
            self.screenshot_as_file()

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

    #鼠标键盘操作
    def move_to_element_by_mouse(self,element_info):
        element=self.find_element(element_info)
        ActionChains(self.driver).move_to_element(element).perform()

    def long_press_element(self,element_info,seconds):
        element=self.find_element(element_info)
        ActionChains(self.driver).click_and_hold(element).pause(seconds).release(element).perform()

#截图操作
    def screenshot_as_file_old(self,*screenshot_path):
        current_dir = os.path.dirname(__file__)
        if len(screenshot_path) == 0:
            screenshot_filepath = read_config.screenshot_path
        else:
            screenshot_filepath = screenshot_path[0]
        now = time.strftime('%Y_%m_%d_%H_%M_%S')
        screenshot_filepath = os.path.join(current_dir,'..',screenshot_filepath,'UITest_%s.png'%now)
        self.driver.get_screenshot_as_file(screenshot_filepath)
        log_pri.info('截图，存放在地址%s'%screenshot_filepath)

    def screenshot_as_file(self):
        report_path = os.path.join(os.path.dirname(__file__),'..',read_config.get_report_path)
        report_dir = HTMLTestReportCN.ReportDirectory(report_path)
        report_dir.get_screenshot(self.driver)
        log_pri.info('截图，存放在地址%s'%report_path)




