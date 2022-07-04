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


read_config=ConfigUtils()

if __name__=='__main__':
    read_config = ConfigUtils()
    print(read_config.get_url)
    print(read_config.driver_path)
    print(read_config.driver_name)