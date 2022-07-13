#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/11 0011 21:20
import os
from common.excel_utils import ExcelUtils
from common.config_utils import read_config

current_path = os.path.dirname(__file__)
dir_path = os.path.join(current_path, '..', read_config.get_test_datas_path)


class TestDataUtils:
    def __init__(self, test_suite_name, test_class_name):
        self.test_class_name = test_class_name
        self.excel_utils = ExcelUtils(dir_path, sheet_name=test_suite_name)
        self.excel_datas = self.excel_utils.get_sheet_data_by_list()
        self.testsuite_counts = len(self.excel_datas)

    def convert_exceldata_to_testdata(self):
        test_data_infos = {}
        for i in range(1,self.testsuite_counts):
            if self.excel_datas[i][2] == self.test_class_name:
                test_data_info={}
                test_data_info['test_name']=self.excel_datas[i][1]
                test_data_info['isnot']=False if self.excel_datas[i][3].__eq__('是') else True
                test_data_info['excepted_result'] = self.excel_datas[i][4]
                test_parameter = {}
                for j in range(5,len(self.excel_datas[i])):
                    if self.excel_datas[i][j]=='':
                        break
                    test_parameter[self.excel_datas[i][j].split('=')[0]]=self.excel_datas[i][j].split('=')[1]
                    test_data_info['test_parameter']=test_parameter
                test_data_infos[self.excel_datas[i][0]]=test_data_info
        return test_data_infos

if __name__ == '__main__':
    test1=TestDataUtils('login_suite','LoginTest')
    print(test1.convert_exceldata_to_testdata())
    for i in test1.convert_exceldata_to_testdata().values():
        print(i)

