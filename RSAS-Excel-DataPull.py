#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import xlrd
import xlwt
from xlrd import open_workbook
from  xlutils.copy import copy
# encoding=utf8
import sys


###########################################################
# 创建workbook和sheet对象
workbook = xlwt.Workbook()  # 注意Workbook的开头W要大写
sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
# 向sheet页中写入数据
sheet1.write(0, 0, u'IP地址')
sheet1.write(0, 1, u'端口')
sheet1.write(0, 2, u'服务')
sheet1.write(0, 3, u'URL')
sheet1.write(0, 4, u'操作系统')
# 保存该excel文件,有同名文件时直接覆盖
name= raw_input('输入文件名称: '.decode('utf-8').encode('gbk'));
path='D:/'+name+'.xls'
workbook.save(path)
print '创建excel文件完成！'
seq = 1
############################################################
def openexcel(str):
    # 打开一个EXCEL文件
    excel = xlrd.open_workbook(str)
    # 获取第一个sheet
    sheet0 = excel.sheets()[0]
    ip = sheet0.cell(2, 1).value
    # 获取第三个sheet
    sheet = excel.sheets()[2]
    nrows = sheet.nrows  # sheet行数
    dictionary = {}
    osname=''
    if nrows>3 and nrows<200:#判断是否有开放端或者是否有防火墙
        for i in range(0, nrows):
            row = sheet.row_values(i)
            # print row
            # print  row[0]
            if row[0] == u'\u7aef\u53e3Banner':
                print i
                banner = i
            elif row[0] == u'\u7aef\u53e3\u4fe1\u606f':
                print i
                port = i
            elif row[0] == u'\u64cd\u4f5c\u7cfb\u7edf\u7c7b\u578b':
                print i
                os = i
                osname=sheet.cell(i+2, 1).value
            else:
                continue
        for i in range(port + 2, os):
            # print sheet.row_values(i)
            if sheet.cell(i, 3).value!='unknown':#过滤未知端口
                dictionary[sheet.cell(i, 1).value] = sheet.cell(i, 3).value
    return ip,dictionary,osname
##########################################################################
def WirteinExcel(str):
    result = openexcel(str)
    old = xlrd.open_workbook(path,formatting_info=True)
    new = copy(old)
    tmp=len(result[1])
    sheet = new.get_sheet(0)
    if tmp==1 or tmp==0:
        sheet.write(seq,0, result[0])
    else:
        sheet.write_merge(seq, seq+tmp-1, 0, 0, result[0])
    for key, value in result[1].items():
        print key, value
        global seq
        sheet.write(seq, 1, key)
        sheet.write(seq, 2, value)
        if value == 'http' or value == "https":
            sheet.write(seq, 3, 'http://' + result[0] + ':' + key)
            if key == '443' or value == 'https':
                sheet.write(seq, 3, 'https://' + result[0] + ':' + key)
        sheet.write(seq,4,result[2])
        seq = seq + 1
        new.save(path)
##############################################################################
def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            GetFileList(newDir, fileList)
    return fileList
###############################################################################
list = GetFileList('D:/qhyd/'+name, [])
for e in list:
    print e
    WirteinExcel(e)
    print e+u'处理完成！'
