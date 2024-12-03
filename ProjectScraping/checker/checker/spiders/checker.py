import scrapy


class CheckerSpider(scrapy.Spider):
    name = "checker"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/computer/igrovye-pristavki/"]

    def parse(self, response):
        titles = response.xpath('//a[@class="item-title"]/text()').getall()
        for title in titles:
            yield {
                'title': title
            } 