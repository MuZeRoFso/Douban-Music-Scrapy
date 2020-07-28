# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time

from scrapy.exporters import XmlItemExporter


class DoubanmusicPipeline(object):
    # 创建一个构造方法，定义输出文件的文件夹
    def __init__(self):
        # 定义输出文件夹
        self.folderName = 'output'
        now = time.strftime('%Y-%m-%d', time.localtime())
        xmlFileName = 'doubanmusic_' + now + '.xml'
        self.xmlfile = open(self.folderName + '/' + xmlFileName, 'wb')
        # 指定xml输出文件 item_element为根目录下第一级子元素 root_element是根目录名称
        self.exporter = XmlItemExporter(
            self.xmlfile, item_element='music', root_element='musicinfo', indent=4)
        # 开始输出
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        # 提示用户开始到处Json文件
        print('>> item写入XML文件......')
        try:
            self.exporter.export_item(item=item)
        except Exception as err:
            # 打印错误信息
            print('XML导入出错: {0}'.format(str(err)))
        return item

    def close_spider(self, spider):
        # 结束输出
        self.exporter.finish_exporting()
        # 关闭文件
        self.xmlfile.close()
        pass
