import scrapy
from xiuren.items import XiurenItem


class xiu_ren_spider(scrapy.Spider):
    name = "xiuren"
    allowed_domains = ["xiuren.org"]

    start_urls = [
        "http://www.xiuren.org/",
        #"http://www.xiuren.org/page-2.html"
        "http://www.xiuren.org/page-3.html",
        "http://www.xiuren.org/page-4.html",
        "http://www.xiuren.org/page-5.html",
        "http://www.xiuren.org/page-6.html",
        "http://www.xiuren.org/page-7.html",
        "http://www.xiuren.org/page-8.html",
        "http://www.xiuren.org/page-9.html",
        "http://www.xiuren.org/page-10.html",
        "http://www.xiuren.org/page-11.html",
        "http://www.xiuren.org/page-12.html",
        "http://www.xiuren.org/page-13.html",
        "http://www.xiuren.org/page-14.html",
        "http://www.xiuren.org/page-15.html",
        "http://www.xiuren.org/page-16.html"
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
