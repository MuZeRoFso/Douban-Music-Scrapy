# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class DoubanmusicPipeline(object):
    def process_item(self, item, spider):
        connection = ''
        try:
            # 创建数据库连接
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='123456',
                                         db='doubanmusic', charset='utf8')
            if connection:
                print('>> 成功连接数据库')
            # 创建一个游标
            cursor = connection.cursor()
            sql = 'insert into music values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")' % (item['title'],
                   item['author'], item['publish'], item['album'], item['disc'], item['style'],item['score'], item['pic_url'])
            # 执行sql语句并返回结果
            affectedRows = cursor.execute(sql)
            msg = '>> item写入成功' if affectedRows > 0 else '>> item写入失败'
            print(msg)
            connection.commit()
        except:
            connection.rollback()
        connection.close()
        return item
