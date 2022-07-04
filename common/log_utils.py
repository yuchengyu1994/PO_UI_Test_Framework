import os
import logging


current_path=os.path.dirname(__file__)
log_path= os.path.join(current_path, '../logs/test.log')
class LogUtils:
    def __init__(self,logfile_path=log_path):
        self.logfile_path=logfile_path
        self.logger=logging.getLogger()
        # self.logger.handlers.clear()
        self.logger.setLevel(level= logging.INFO)
        file_log = logging.FileHandler(self.logfile_path,encoding='utf-8')
        formatter = logging.Formatter('file:%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)

    def info(self,info_msg):
        self.logger.info(info_msg)

    def error(self,error_msg):
        self.logger.error(error_msg)
log_pri=LogUtils()
if __name__=='__main__':
    log1=LogUtils()
    log1.info('newdream123')
    # log1.error('1234')


