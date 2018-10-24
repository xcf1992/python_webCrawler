import scrapy
from xiuRenOrg.items import SubPageItem

class xiu_ren_spider(scrapy.Spider):
    name = "xiu_ren"
    allowed_domains = ["xiuren.org"]

    start_urls = [
        "http://www.xiuren.org/",
        "http://www.xiuren.org/page-2.html",
        "http://www.xiuren.org/page-3.html",
        "http://www.xiuren.org/page-4.html",
        "http://www.xiuren.org/page-5.html",
        "http://www.xiuren.org/page-6.html",
        "http://www.xiuren.org/page-7.html",
        "http://www.xiuren.org/page-8.html",
        "http://www.xiuren.org/page-9.html",
        "http://www.xiuren.org/page-10.html",
        "http://www.xiuren.org/page-11.html"
    ]


    def parse(self, response):

        for href in response.css("body > div > div > div > div > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_sub_page)

        return

    def parse_sub_page(self, response):
        item = SubPageItem()
        item["title"] = response.xpath('//title/text()').extract_first()
        item["img_link"] = []
        for sel in response.xpath('//span'):
            link = sel.xpath('a/@href').extract_first()
            if link:
                item["img_link"].append(link)

        return item
