from pathlib import Path

import scrapy

class GrocerySpider(scrapy.Spider):
    name = "cafe"
    allowed_domains = ["cafef.vn"]
    start_urls = ["https://cafef.vn/tai-chinh-quoc-te.chn"]

    def parse(self, response):
        list_products = response.css('div.tlitem.box-category-item')
        
        for product in list_products:
            yield {
                'title': product.css('div.tlitem-flex a::attr(title)').get(),
                'link': product.css('h3 a::attr(href)').get()
            }

