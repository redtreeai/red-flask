# -*- coding: utf-8 -*-
# @Time    : 19-4-10 下午3:18
# @Author  : Redtree
# @File    : xls_tool.py
# @Desc : excel表格文件处理工具

import xlrd #xls文件流读取工具

def xls_reader(filepath,x,y):
    xls_file = xlrd.open_workbook(filepath)  #打开文件
    xls_sheet = xls_file.sheets()[0] #打开工作谱

    row_value = xls_sheet.row_values(x) #按行读取
    col_value = xls_sheet.col_values(y)#按列读取
    value = xls_sheet.cell(x, y).value #定位读取

    print(xls_sheet.nrows)   #总行数
    print(row_value,col_value,value)


def xls2list (filepath):
    try:
        xls_file = xlrd.open_workbook(filepath)  # 打开文件
        xls_sheet = xls_file.sheets()[0]  # 打开工作谱
        n = xls_sheet.nrows

        res = []
        for x in range(0, n):
            c_obj = xls_sheet.row_values(x)
            res.append(c_obj)
        return res

    except:
        return []


#xls2list('t1.xlsx')