# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HearthstoneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    english_name = scrapy.Field()
    color = scrapy.Field()
    image_url = scrapy.Field()
    type = scrapy.Field()
    char = scrapy.Field()
    skill_type = scrapy.Field()
    description = scrapy.Field()
    cost = scrapy.Field()
    attack = scrapy.Field()
    health = scrapy.Field()

