# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanmusicPipeline(object):
    def process_item(self, item, spider):
        print('>> 输出歌曲信息')
        print('\t歌曲名:{0}'.format(item['title']))
        print('\t作者:{0}'.format(item['author']))
        print('\t出版时间:{0}'.format(item['publish']))
        print('\t歌曲类型:{0}'.format(item['album']))
        print('\t碟片类型:{0}'.format(item['disc']))
        print('\t风格:{0}'.format(item['style']))
        print('\t评分:{0}'.format(item['score']))
        print('\t图片:{0}'.format(item['pic_url']))
        print()
        return item
