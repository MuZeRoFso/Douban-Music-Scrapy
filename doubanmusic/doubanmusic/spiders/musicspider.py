# -*- coding: utf-8 -*-
import scrapy
# 引入DoubanmusicItem类
from doubanmusic.items import DoubanmusicItem


class MusicspiderSpider(scrapy.Spider):
    name = 'musicspider'
    allowed_domains = ['douban.com']
    # 需要爬取的网站 豆瓣音乐top250
    start_urls = ['https://music.douban.com/top250']

    def parse(self, response):
        # item代码块 XPath //div[@class="pl2"]
        # 标题 XPath td[2]/div[class="pl2"]/a/text()
        # 分类描述 XPath td[2]/div[class="pl2"]/p/text()
        # 评分 XPath td[2]/div[class="pl2"]/div[@class="star clearfix"]/span[@class="rating_nums"]/text()
        music_items = response.xpath('//tr[@class="item"]')
        # 循环遍历所有的音乐item，获取其中的标题 分类描述信息 评分数值
        for item in music_items:
            # 创建空的DoubanmusicItem对象
            music = DoubanmusicItem()
            # 为music对象的属性赋值
            music['title'] = item.xpath('td[2]/div/a/text()').extract()[0].strip()
            desclist = item.xpath('td[2]/div/p/text()').extract()[0].split(' / ')
            music['author'] = desclist[0]
            music['publish'] = desclist[1]
            music['album'] = desclist[2] if len(desclist) == 4 or desclist[2] != 'CD' else '专辑'
            music['disc'] = desclist[3] if len(desclist) == 4 else 'CD'
            music['style'] = desclist[4] if len(desclist) == 5 else '暂无'
            music['score'] = item.xpath('td[2]/div/div/span[2]/text()').extract()[0]
            music['pic_url'] = item.xpath('td[1]/a/img/@src').extract()[0]
        pass
