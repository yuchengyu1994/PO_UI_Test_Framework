import os
import configparser


current_path = os.path.dirname(__file__)
config_path=os.path.join(current_path,'../conf/config.ini')

class ConfigUtils:
    def __init__(self,conf_path=config_path):
        # self.conf_data=configparser.ConfigParser().read(conf_path)
        self.conf = configparser.ConfigParser()
        self.conf.read(conf_path,encoding='utf-8')


    @property
    def get_url(self):
        url_value=self.conf.get('default','url')
        return url_value

    @property
    def driver_path(self):
        return self.conf.get('default','driver_path')

    @property
    def driver_name(self):
        return self.conf.get('default','driver_name')

    @property
    def get_log_path(self):
        return self.conf.get('default', 'log_path')

    @property
    def get_log_level(self):
        return int(self.conf.get('default', 'log_level'))

    @property
    def time_out(self):
        return float(self.conf.get('default','time_out'))

    @property
    def screenshot_path(self):
        return self.conf.get('default', 'screenshot_path')

    @property
    def get_username(self):
        return self.conf.get('default', 'username')


    @property
    def get_password(self):
        return self.conf.get('default', 'password')

    @property
    def get_test_datas_path(self):
        return self.conf.get('default', 'test_datas_path')

    @property
    def get_case_path(self):
        return self.conf.get('default', 'case_path')

    @property
    def get_report_path(self):
        return self.conf.get('default', 'report_path')


read_config=ConfigUtils()

if __name__=='__main__':
    read_config = ConfigUtils()
    print(read_config.get_url)
    print(read_config.driver_path)
    print(read_config.driver_name)
    print(read_config.time_out)
    print(read_config.get_log_level)
    print(read_config.get_test_datas_path)
