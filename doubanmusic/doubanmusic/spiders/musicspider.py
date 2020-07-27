# -*- coding: utf-8 -*-
import scrapy
# 引入DoubanmusicItem类
from doubanmusic.items import DoubanmusicItem


class MusicspiderSpider(scrapy.Spider):
    name = 'musicspider'
    allowed_domains = ['douban.com']
    # 需要爬取的网站 豆瓣音乐top250
    start_urls = ['https://www.douban.com/']

    def parse(self, response):
        pass
