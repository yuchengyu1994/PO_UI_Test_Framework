#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/12 0012 12:00
import os
import unittest
from  common import HTMLTestReportCN
from common.config_utils import read_config
from common.email_utils import EmailUtils
from common import zip_utils


current_path=os.path.dirname(__file__)
report_path=os.path.join(current_path,'..',read_config.get_report_path)
case_path=os.path.join(current_path,'..',read_config.get_case_path)
class RunAllCases:
    def __init__(self):
        self.test_case_path=case_path
        self.report_path=report_path
        self.title='禅道自动化测试报告'
        self.description = 'YuChengyu-test'

    def run(self):
        discover= unittest.defaultTestLoader.discover(start_dir=self.test_case_path,\
                                                      pattern='*_test.py',top_level_dir=self.test_case_path)

        all_suite= unittest.TestSuite()
        all_suite.addTest(discover)

        report_dir=HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        dir_path=HTMLTestReportCN.GlobalMsg.get_value('dir_path')
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp =open(report_path,'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester='Yu')
        runner.run(all_suite)
        fp.close()
        return dir_path

if __name__ == '__main__':
    dir_path=RunAllCases().run()
    zip_path=os.path.join(dir_path,'..','自动化测试报告.zip')
    zip_utils.zip_utils(dir_path,zip_path)
    print(zip_path)
    email_utils = EmailUtils('自动化测试报告','来自python邮件自动发送测试',smtp_file_path=zip_path)
    email_utils.send_mail()