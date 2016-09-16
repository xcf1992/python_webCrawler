import scrapy
from xiuRenOrg.items import MainPageItem
from xiuRenOrg.items import SubPageItem

class main_page_spider(scrapy.Spider):
    name = "main_page"
    allowed_domains = ["xiuren.org"]
    start_urls = ["http://www.xiuren.org/"]
    
    def parse(self, response):
        for href in response.css("body > div > div > div > div > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_sub_page)

    def parse_sub_page(self, response):
        item = SubPageItem()
        item["title"] = response.xpath('//title/text()').extract()
        item["img_link"] = []
        for sel in response.xpath('//span'):
            link = sel.xpath('a/@href').extract()
            if link:
                item["img_link"].append(link)

        yield item
