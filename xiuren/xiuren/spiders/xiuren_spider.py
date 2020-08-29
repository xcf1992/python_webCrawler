import scrapy
from xiuren.items import XiurenItem

class xiu_ren_spider(scrapy.Spider):
    name = "xiuren"
    allowed_domains = ["xiuren.org"]

    start_urls = [
        "http://www.xiuren.org/"
    ]

    def parse(self, response):
        for href in response.css("body > div > div > div > div > a::attr('href')"):
            url = response.urljoin(href.extract())
            if url in ["http://www.xiuren.org/tuigirl-special-lilisha-double.html", "http://www.xiuren.org/shanshan-xianrou.html", "http://www.xiuren.org/okamoto-002.html"]:
                continue
            #print(f"{url}")
            yield scrapy.Request(url, callback=self.parse_sub_page)

    def parse_sub_page(self, response):
        item = XiurenItem()
        item["urls"] = response.css("body > div > div > div > div > p > span > a::attr('href')").extract()
        item["name"] = response.css("body > div > div > div > div > h1::text").extract_first()
        yield item