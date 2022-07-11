import os
import xlrd2
from common.config_utils import read_config
from common.excel_utils import ExcelUtils

current_path=os.path.dirname(__file__)
excel_path=os.path.join(current_path,'../element_info_datas/elment_data.xlsx')

#
class ElementDataUtils:
    def __init__(self,module_name,page_name,file_path=excel_path):
        self.file_path=file_path
        self.page_name = page_name
        self.workbook = xlrd2.open_workbook(self.file_path)
        self.sheet = self.workbook.sheet_by_name(module_name)


# print(sheet.cell_value(3,1))

# print(element_infos)
# element_info={}

    def get_element_info1(self,element_name):
        element_infos={}
        for i in range(1, self.sheet.nrows):
            element_info = {}
            for j in range(1,self.sheet.ncols):
                element_info[self.sheet.cell_value(0, j)]=self.sheet.cell_value(i, j)
                # print(element_info)
            element_infos[self.sheet.cell_value(i, 0)]=element_info
            return element_infos[element_name]

    def get_element_info(self):
        element_infos = {}
        for i in range(1, self.sheet.nrows):
            if self.sheet.cell_value(i,2) == self.page_name:
                element_info = {}
                element_info['element_name'] = self.sheet.cell_value(i, 1)
                element_info['locator_type'] = self.sheet.cell_value(i, 3)
                element_info['locator_value'] = self.sheet.cell_value(i, 4)
                element_info['timeout'] =  self.sheet.cell_value(i, 5) if\
                    isinstance(self.sheet.cell_value(i, 5),float) else read_config.time_out
                element_infos[self.sheet.cell_value(i, 0)] = element_info
        return element_infos



if __name__=='__main__':
    elements=ElementDataUtils('login','main_page').get_element_info()
    print(elements)

