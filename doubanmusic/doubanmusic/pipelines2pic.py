# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib


class DoubanmusicPipeline(object):
    def __init__(self):
        # 定义输出图片的文件夹
        self.folderName = 'output/pic'
        # 判断该文件夹是否存在，不存在则创建
        if not os.path.exists(self.folderName):
            os.mkdir(self.folderName)

    def process_item(self, item, spider):
        print('>>开始下载图片至本地......')
        # 获取图片url
        pic_url = item['pic_url']
        # 设置图片名字
        pic_type = pic_url.split('.')[-1]
        pic_name = item['title'] + '.' + pic_type
        print('>>开始下载', pic_name)
        try:
            # 开始下载图片
            urllib.request.urlretrieve(pic_url, self.folderName + "/%s" % pic_name)
        except Exception as e:
            print('下载出现错误: ', str(e))

        return item
