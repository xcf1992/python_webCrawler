import scrapy
from nvshen.items import NvshenItem

class MeituriSpider(scrapy.Spider):
    name = "nvshen"
    allowed_domian = "xsnvshen.com"

    start_urls = [
                    "https://www.xsnvshen.com/girl/19411"
                 ]

    def parse(self, response):
        for href in response.css("body > div > div > div > div > div > ul > li > a::attr('href')").extract():
            if "album" not in href:
                continue
            next_url = f"{response.urljoin(href)}"
            yield scrapy.Request(next_url, callback=self.parse_sub_page)

    def parse_sub_page(self, response):
        item = NvshenItem()
        item["urls"] = response.css("body > div > div > div > ul > li > div > img::attr('src')").extract()
        item["names"] = response.css("body > div > div > div > ul > li > div > img::attr('alt')").extract()
        yield item
