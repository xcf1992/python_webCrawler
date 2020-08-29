import scrapy
from xiuren.items import XiurenItem


class xiu_ren_spider(scrapy.Spider):
    name = "xiuren"
    allowed_domains = ["xiuren.org"]

    start_urls = [
        "http://www.xiuren.org/page-17.html",
        "http://www.xiuren.org/page-18.html",
        "http://www.xiuren.org/page-19.html",
        "http://www.xiuren.org/page-20.html",
        "http://www.xiuren.org/page-21.html",
        "http://www.xiuren.org/page-22.html",
        "http://www.xiuren.org/page-23.html",
        "http://www.xiuren.org/page-24.html",
        "http://www.xiuren.org/page-25.html",
        "http://www.xiuren.org/page-26.html",
        "http://www.xiuren.org/page-27.html",
        "http://www.xiuren.org/page-28.html",
        "http://www.xiuren.org/page-29.html",
        "http://www.xiuren.org/page-30.html",
        "http://www.xiuren.org/page-31.html",
        "http://www.xiuren.org/page-32.html"
    ]

    def parse(self, response):
        for url in response.css("body > div > div > div > div > a::attr('href')").extract():
            if url in ["http://www.xiuren.org/tuigirl-special-lilisha-double.html", "http://www.xiuren.org/shanshan-xianrou.html", "http://www.xiuren.org/okamoto-002.html"]:
                continue
            #print(f"{url}")
            yield scrapy.Request(url, callback=self.parse_sub_page)

    def parse_sub_page(self, response):
        item = XiurenItem()
        item["urls"] = response.css("body > div > div > div > div > p > span > a::attr('href')").extract()
        item["name"] = response.css("body > div > div > div > div > h1::text").extract_first()
        yield item
