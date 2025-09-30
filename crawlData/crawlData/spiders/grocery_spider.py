from pathlib import Path

import scrapy

class GrocerySpider(scrapy.Spider):
    name = "grocery"
    allowed_domains = ["webtaphoa.vn"]
    start_urls = ["https://www.webtaphoa.vn/collections/all"]

    def parse(self, response):
        list_products = response.css('div.product-item')
        
        for product in list_products:
            yield {
                'name': product.css('h3.pro-name a::attr(title)').get(),
                'price': product.css('span.current-price::text').get(default="").replace('₫', '').strip(),
                'link': response.urljoin(product.css('h3.pro-name a::attr(href)').get()),
            }

        next_page = response.css('a.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
