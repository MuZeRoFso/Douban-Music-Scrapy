# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time

from scrapy.exporters import JsonItemExporter


class DoubanmusicPipeline(object):
    # 创建一个构造方法，定义输出文件的文件夹
    def __init__(self):
        # 定义输出文件夹
        self.folderName = 'output'
        now = time.strftime('%Y-%m-%d', time.localtime())
        jsonFileName = 'doubanmusic_' + now + '.json'
        self.jsonfile = open(self.folderName + '/' + jsonFileName, 'wb')
        self.exporter = JsonItemExporter(self.jsonfile, encoding="utf-8", ensure_ascii=False, indent=4)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        # 提示用户开始导出Json文件
        print('>> item写入Json文件......')
        try:
            self.exporter.export_item(item)
        except Exception as err:
            # 打印错误信息
            print('Json导入出错: {0}'.format(str(err)))
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.jsonfile.close()
        pass
