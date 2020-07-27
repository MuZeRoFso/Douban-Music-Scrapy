# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmusicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 音乐(专辑)标题
    author = scrapy.Field()  # 歌曲作者
    publish = scrapy.Field()  # 出版时间
    album = scrapy.Field()  # 专辑类型：单曲/专辑
    disc = scrapy.Field()  # 碟片类型 CD DVD
    style = scrapy.Field()  # 曲风
    score = scrapy.Field()  # 评分
    pic_url = scrapy.Field()  # 歌曲封面图片Url
    pass
