import scrapy

from file_download.items import DownloadFilesItem

class GetFilesSpider(scrapy.Spider):
    name = 'get_files'
    allowed_domains = ['docs.python.org']
    start_urls = ['https://docs.python.org/2/archives/']
    base_url = 'https://docs.python.org/2/archives/'

    def parse(self, response):
        for link in response.xpath('/html/body/pre/a'):
            all_url = self.base_url + link.xpath('.//@href').get()
            allowed = 'html.zip'
            if allowed in all_url:
                url = response.urljoin(all_url)
                item = DownloadFilesItem()
                item['file_urls'] = [url]
                yield item