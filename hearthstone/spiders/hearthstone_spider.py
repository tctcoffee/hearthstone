#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
# File Name: hearthstone/spiders/hearthspide_spider.py
# Author: YourName
# mail: YourEmail
# Created Time: 2016-04-05

from scrapy.spider import Spider
from scrapy.selector import Selector
from hearthstone.items import HearthstoneItem
from scrapy.http import Request
import codecs

class HearthstoneSpider(Spider):
    name = "hearthstone"
    allow_domains = ["duowan.com"]
    start_urls = ["http://db.duowan.com/lushi/card/list/"]
    
    def parse(self,response):
        sel = Selector(response)
        next_url = sel.xpath('//div/a[@rel="next"]/@href').extract()[0].encode('utf-8')
        self.start_urls.append(next_url)
        dates = sel.xpath('//tbody/tr')
        items = []
        for data in dates:
            item = HearthstoneItem()
            item['name'] = data.xpath('td[@class="name"]/a/text()').extract()[0].encode('utf-8')
            item['english_name'] = data.xpath('td[@class="name"]/a/@data-src').extract()[0].split('/')[-1].split('.')[0].encode('utf-8')
            if data.xpath('td[@class="name"]/a/@style')==[]:
                item['color'] = "color:#008000"
            else:
                item['color'] = data.xpath('td[@class="name"]/a/@style').extract()[0].encode('utf-8')
            item['image_url'] = data.xpath('td[@class="name"]/a/@data-src').extract()[0].encode('utf-8')
            item['type'] = data.xpath('td[5]/text()').extract()[0].encode('utf-8')
	    item['char'] = data.xpath('td[4]/text()').extract()[0].encode('utf-8')
            #比如战吼技能，有的没有，就需要做一个判断   另外，多个技能如何解决？
            if data.xpath('count(td[@class="skill"]/a)').extract()[0].encode('utf-8')=='0.0':
                item['skill_type'] = "None"
            else:
                item['skill_type'] = data.xpath('td[@class="skill"]/a/@data-tips').extract()[0].encode('utf-8')
            #卡牌的描述，有的没有，也需要一个判断......
            if data.xpath('td[3]/text()')==[]:
                item['description'] = "None"
            else:
                item['description'] = data.xpath('td[3]/text()').extract()[0].encode('utf-8')
            item['cost'] = data.xpath('td[6]/text()').extract()[0].encode('utf-8')
            item['attack'] = data.xpath('td[7]/text()').extract()[0].encode('utf-8')
	    item['health'] = data.xpath('td[8]/text()').extract()[0].encode('utf-8')
            items.append(item)
        return items
