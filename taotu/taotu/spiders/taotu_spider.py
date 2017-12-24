import scrapy
from taotu.items import TaotuItem


class TaotuSpider(scrapy.Spider):
    name = "taotu"

    _BASE_URL = "https://www.aitaotu.com"

    start_urls = [
        "https://www.aitaotu.com/tag/ttns/2.html",
        "https://www.aitaotu.com/tag/ttns/3.html",
        "https://www.aitaotu.com/tag/ttns/4.html",
        "https://www.aitaotu.com/tag/ttns/5.html",
        "https://www.aitaotu.com/tag/ttns/6.html",
        "https://www.aitaotu.com/tag/ttns/7.html",
        "https://www.aitaotu.com/tag/ttns/8.html",
        "https://www.aitaotu.com/tag/ttns/9.html",
        "https://www.aitaotu.com/tag/ttns/10.html"
    ]

    def parse(self, response):
        data = response.css("body > div > div > div > div")[4]
        subs = data.css("ul > li > a::attr('href')").extract()
        for sub_url in subs:
            url = "%s%s" % (self._BASE_URL, sub_url)
            yield scrapy.Request(url, callback=self.parse_sub_page)
        return

    def parse_sub_page(self, response):
        item = TaotuItem()

        header = response.css("body > div > div > div")[3]
        title = header.css("h1::text").extract_first()

        image = response.css("body > div > div > div > div > p > a > img::attr('src')").extract()

        nav = response.css("body > div > div > div")[10]
        next_page = nav.xpath("//div/ul/li[@id='nl']/a/@href").extract_first()

        item["title"] = title
        item["image"] = image

        yield item
        if next_page:
            next_url = "%s%s" % (self._BASE_URL, next_page)
            yield scrapy.Request(next_url, callback=self.parse_sub_page)
