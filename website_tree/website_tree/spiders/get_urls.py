import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.crawler import CrawlerProcess


class GetUrlsSpider(SitemapSpider):
    name = 'get_urls'
    allowed_domains = ['princetonscientific.com']
    sitemap_urls = ['https://princetonscientific.com/sitemap_index.xml']

    def parse(self, response):
        page_title = response.css('title::text').get()
        page_url = response.url
        urls = {
            page_title: page_url
        }

        file = "output/url-list.txt"
        with open(file, "a") as stream:
            for v in urls.values():
                stream.write(v + "\n")

        yield urls

def run_spider():
    process = CrawlerProcess(settings={
        "FEEDS": {
            "output/titles-url-list.jl": {"format": "jl"},
        },
    })

    process.crawl(GetUrlsSpider)
    process.start() # the script will block here until the crawling is finished
    print("\n\n\n")
    input("Crawling finished. Press any key to return to the menu: ")