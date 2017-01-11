# -*- coding: utf-8 -*-
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from stack.items import StackItem


class QuestionsSpider(CrawlSpider):
    name = 'head'
    allowed_domains = ['bbc.com']
    start_urls = [
        'http://www.bbc.com/'
    ]

    def parse_item(self, response):
        heads = response.xpath('//figure[@class="media-landscape"]/h3')

        for head in heads:
            item = StackItem()
            item['title'] = head.xpath(
                'h1[@class="story-body__h1"]/@href').extract()[0]
            item['url'] = head.xpath(
                'a[@class="index-title__container"]/@href').extract()[0]
            item['author'] = head.xpath(
                'a[@class="story-body__link-external"]/text()').extract()[0]
            yield item
