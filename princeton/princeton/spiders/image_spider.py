import scrapy
from princeton.items import ImageItem


class ImageSpiderSpider(scrapy.Spider):
    name = 'image_spider'
    allowed_domains = ['www.princetonscientific.com']
    start_urls = ['https://www.princetonscientific.com/']

    def parse(self, response):
        item = ImageItem()
        if response.status == 200:
            rel_img_urls = response.css('img::attr(src)').extract()
            item['image_urls'] = self.url_join(rel_img_urls, response)
        return item

    def url_join(self, rel_img_urls, response):
        joined_urls = []
        for rel_img_url in rel_img_urls:
            joined_urls.append(response.urljoin(rel_img_url))

        return joined_urls
