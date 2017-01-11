from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from stack.items import StackItem


class StackSpider(CrawlSpider):
    name = "stackcrawl"
    allowed_domains = ["bbc.com"]
    start_urls = [
        "http://www.bbc.com/",
    ]
    rules = (
        Rule(
            SgmlLinkExtractor(allow=('&page=\d')),
            callback='parse',
            follow=True
        ),
    )

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        questions = hxs.xpath('//div[@class="media__title"]/h3')
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="media__link"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="media__link"]/@href').extract()[0]
            yield item
