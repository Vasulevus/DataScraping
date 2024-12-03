import scrapy


class ConsolesSpider(scrapy.Spider):
    name = "consoles"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/computer/igrovye-pristavki/"]

    current = 0
    max_page = 1

    def parse(self, response):
        titles = response.xpath('//a[@class="item-title"]/text()').getall()
        for title in titles:
            yield {
                'title': title
            } 

#    def parse(self, response):
#        quotes = response.xpath('//span[@class="text"]/text()').getall()
#        authors = response.xpath("//small[@class='author']/text()").getall()
#        #for author in authors:
#        for quote, author in zip(quotes, authors):
#            yield {
#                'text' : quote,
#                'author': author
#            }
#
#        next_page = response.xpath('//li[@class="next"]/a/@href').get()
#        if next_page is not None and self.current < self.max_page:
#            self.current += 1
#            yield response.follow(next_page, callback=self.parse)
#