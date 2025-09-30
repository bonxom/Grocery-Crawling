from pathlib import Path

import scrapy

class GrocerySpider(scrapy.Spider):
    name = "grocery"
    allowed_domains = ["webtaphoa.vn"]
    start_urls = ["https://www.webtaphoa.vn/collections/all"]