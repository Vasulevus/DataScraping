import scrapy


class CheckerSpider(scrapy.Spider):
    name = "checker"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua"]

    def parse(self, response):
        pass
