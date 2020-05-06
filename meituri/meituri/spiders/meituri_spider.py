import scrapy
from meituri.items import MeituriItem


class MeituriSpider(scrapy.Spider):
    name = "meituri"
    allowed_domian = "meituri.com"

    start_urls = [
                    "https://www.lanvshen.com/t/2712/",
                    "https://www.lanvshen.com/t/2712/index_1.html"
                 ]

    def parse(self, response):
        for href in response.css("body > div > ul > li > a::attr('href')")[0:-5]:
            next_url = response.urljoin(href.extract())
            yield scrapy.Request(next_url, callback=self.parse_sub_page)

    def parse_sub_page(self, response):
        next_page = response.css("body > center > div > a::attr('href')").extract()
        print(f"[parse_sub_page] next_page is {next_page}")
        if len(next_page) == 0:
            return

        next_page = next_page[-1]
        current_url = response.request.url
        print(f"[parse_sub_page] downloading images from {current_url}")

        item = MeituriItem()
        image_urls = response.css("body > div > img::attr('src')").extract()
        image_names = response.css("body > div > img::attr('alt')").extract()
        item["urls"] = image_urls
        item["names"] = image_names

        yield item
        if next_page != current_url:
            yield scrapy.Request(next_page, callback=self.parse_sub_page)
        else:
            print(f"[parse_sub_page] next page is the same current f{current_url}")
