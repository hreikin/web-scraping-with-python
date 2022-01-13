import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GetFilesSpider(CrawlSpider):
    name = 'get_files'
    allowed_domains = ['doc.python.org']
    start_urls = ['https://doc.python.org/']

    rules = (
        Rule(LinkExtractor(allow=r'2/archives/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'3/archives/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
