import scrapy
from tujigu.items import TujiguItem


class TujiguSpider(scrapy.Spider):
    name = "tujigu"
    allowed_domian = "tujigu.com"

    start_urls = [
                    "https://www.tujigu.com/t/5500",
                    "https://www.tujigu.com/t/5500/index_1.html",
                 ]

    def parse(self, response):
        for href in response.css("body > div > ul > li > a::attr('href')").extract():
            if "a" not in href:
                continue
            next_url = f"{response.urljoin(href)}"
            yield scrapy.Request(next_url, callback=self.parse_sub_page)

    def parse_sub_page(self, response):
        item = TujiguItem()
        item["urls"] = response.css("body > div > img::attr('src')").extract()
        item["names"] = response.css("body > div > img::attr('alt')").extract()
        yield item

        cur_page_index = response.css("body > center > div > span::text").get()
        next_page = response.css("body > center > div > a::attr('href')").getall()[-1]
        page_idx = next_page.split("/")[-1].split(".")[0]
        if cur_page_index != page_idx:
            yield scrapy.Request(next_page, callback=self.parse_sub_page)
