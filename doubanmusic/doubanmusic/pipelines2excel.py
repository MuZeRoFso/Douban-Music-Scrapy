# -*- coding: utf-8 -*-

import os
import time

import xlrd
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# python编辑excel文件需要第三方库的支持
# xlwt 负责excel的写入
# xlrd 实现excel的读取
# xlutils 实现对excel的工具包
import xlwt
from xlutils.copy import copy


class DoubanmusicPipeline(object):
    # 构造方法: 创建excel文件模板
    def __init__(self):
        self.foldername = 'output'
        self.filename = 'doubanmusic_' + time.strftime('%Y-%m-%d', time.localtime()) + '.xls'
        # 构造最终文件路径
        self.excelfile = self.foldername + os.sep + self.filename
        # 构造workbook工作簿
        self.workbook = xlwt.Workbook(encoding='utf-8')
        # 构造sheet工作页
        self.sheet = self.workbook.add_sheet(u'豆瓣音乐top250')
        # 设置excel列头
        header = ['标题', '作者', '出版时间', '歌曲类型', '碟片类型', '歌曲风格', '评分', '图片url']
        # 设置列头样式
        headerStyle = xlwt.easyxf('font: color-index black, bold on')
        # 写入列头
        for col in range(0, len(header)):
            self.sheet.write(0, col, header[col], headerStyle)
        # 保存文件
        self.workbook.save(self.excelfile)
        # 全局变量 行数
        self.rowIndex = 1

    def process_item(self, item, spider):
        print('>> item写入Excel文件......')
        # 读入创建好的excel文件
        wb = xlrd.open_workbook(self.excelfile, formatting_info=True)
        # 拷贝一个副本
        newWb = copy(wb)
        sheet = newWb.get_sheet(0)
        # 将数据转换为list类型
        row = [item['title'], item['author'], item['publish'], item['album'], item['disc'], item['style'],
               item['score'], item['pic_url']]
        # for循环输入
        for col in range(0, len(item)):
            # 写入到指定行中
            sheet.write(self.rowIndex, col, row[col])
        # 写入完成
        newWb.save(self.excelfile)
        self.rowIndex += 1
        return item
