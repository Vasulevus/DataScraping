import scrapy


class ConsolesSpider(scrapy.Spider):
    name = "consoles"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua"]

    def parse(self, response):
        pass
