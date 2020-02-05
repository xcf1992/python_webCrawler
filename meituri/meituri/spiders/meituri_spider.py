import scrapy
from meituri.items import MeituriItem


class MeituriSpider(scrapy.Spider):
    name = "meituri"
    allowed_domian = "meituri.com"

    start_urls = ["https://www.meituri.com/t/654/"]

    def parse(self, response):
        for href in response.css("body > div > ul > li > a::attr('href')")[0:-5]:
            next_url = response.urljoin(href.extract())
            yield scrapy.Request(next_url, callback=self.parse_sub_page)

    def parse_sub_page(self, response):
        item = MeituriItem()
        image_urls = response.css("body > div > img::attr('src')").extract()
        image_names = response.css("body > div > img::attr('alt')").extract()
        next_page = response.css("body > center > div > a::attr('href')").extract()[-1]

        item["urls"] = image_urls
        item["names"] = image_names

        yield item
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse_sub_page)
