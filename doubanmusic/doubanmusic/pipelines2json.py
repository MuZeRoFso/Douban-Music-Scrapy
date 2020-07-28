# -*- coding: utf-8 -*-

import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import time


class DoubanmusicPipeline(object):
    # 创建一个构造方法，定义输出文件的文件夹
    def __init__(self):
        # 定义输出文件夹
        self.folderName = 'output'
        # 判断该文件夹是否存在，不存在则创建
        if not os.path.exists(self.folderName):
            os.mkdir(self.folderName)

    def process_item(self, item, spider):
        # 提示用户开始到处Json文件
        print('>> item写入Json文件......')
        # 获取当前时间,并为Json文件命名
        now = time.strftime('%Y-%m-%d', time.localtime())
        jsonFileName = 'doubanmusic_' + now + '.json'
        try:
            # 打开Json文件并写入
            with open(self.folderName + os.sep + jsonFileName, 'a', encoding='utf-8') as jsonfile:
                data = json.dumps(dict(item), ensure_ascii=False) + '\n'
                # 写入data到json文件
                jsonfile.write(data)
        except IOError as err:
            # 打印错误信息
            print('Json文件错误: {0}'.format(str(err)))
        finally:
            jsonfile.close()

        return item
