from scrapy.spiders import SitemapSpider

class PageContentSpider(SitemapSpider):
    name = "page_content"
    sitemap_urls = ['https://princetonscientific.com/sitemap_index.xml']

    def parse(self, response):
        def extract_with_css(query):
            return response.css(query).getall()

        # image_text = extract_with_css('img::attr(alt)')
        image_links = extract_with_css('img::attr(src)')
        pages_linked = extract_with_css('a::attr(href)')
        page_title = response.css('title::text').get()
        # extracted_list = extract_with_css('.siteorigin-widget-tinymce ::text')
        extracted_list = extract_with_css('.entry-content ::text')
        unwanted_items = [
            "609.924.3011",
            "PO Box: 148 | Easton, PA 18044",
            "Fax: 609.924.3018",
            "info@princetonscientific.com",
            "MENU",
            "\n",
            "\t",
            "\n\t"
        ]

        for item in unwanted_items:
            while item in extracted_list:
                extracted_list.remove(item)

        stripped_list = [e for e in extracted_list if len(e.strip()) != 0]
        formatted_list = list(map(str.strip, stripped_list))

        # page_content = {
        #     page_title: formatted_list
        # }
        # yield page_content

        yield {
            'page-title': page_title,
            'page-content': formatted_list,
            'pages-linked': pages_linked,
            # 'image-alt': image_text,
            'image-links': image_links,
        }