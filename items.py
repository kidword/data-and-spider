# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangyuanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    xiaoqu = scrapy.Field()
    jiage  = scrapy.Field()
    mianji = scrapy.Field()
    fukuan = scrapy.Field()
    zhuangxiu = scrapy.Field()
    louceng = scrapy.Field()
    chuzu = scrapy.Field()
    ditie = scrapy.Field()

