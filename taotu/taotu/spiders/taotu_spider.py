import scrapy
from taotu.items import TaotuItem


class TaotuSpider(scrapy.Spider):
    name = "taotu"

    _BASE_URL = "https://www.aitaotu.com"

    start_urls = [
        "https://www.aitaotu.com/tag/youguowang/36.html",
        "https://www.aitaotu.com/tag/youguowang/37.html",
        "https://www.aitaotu.com/tag/youguowang/38.html",
        "https://www.aitaotu.com/tag/youguowang/39.html",
        "https://www.aitaotu.com/tag/youguowang/40.html",
        "https://www.aitaotu.com/tag/youguowang/41.html",
        "https://www.aitaotu.com/tag/youguowang/42.html",
        "https://www.aitaotu.com/tag/youguowang/43.html",
        "https://www.aitaotu.com/tag/youguowang/44.html",
        "https://www.aitaotu.com/tag/youguowang/45.html",
        "https://www.aitaotu.com/tag/youguowang/46.html",
        "https://www.aitaotu.com/tag/youguowang/47.html",
        "https://www.aitaotu.com/tag/youguowang/48.html",
        "https://www.aitaotu.com/tag/youguowang/49.html",
        "https://www.aitaotu.com/tag/youguowang/50.html",
        "https://www.aitaotu.com/tag/youguowang/51.html",
        "https://www.aitaotu.com/tag/youguowang/52.html",
        "https://www.aitaotu.com/tag/youguowang/53.html",
        "https://www.aitaotu.com/tag/youguowang/54.html",
        "https://www.aitaotu.com/tag/youguowang/55.html",
        "https://www.aitaotu.com/tag/youguowang/56.html",
        "https://www.aitaotu.com/tag/youguowang/57.html",
        "https://www.aitaotu.com/tag/youguowang/58.html",
        "https://www.aitaotu.com/tag/youguowang/59.html",
        "https://www.aitaotu.com/tag/youguowang/60.html",
        "https://www.aitaotu.com/tag/youguowang/61.html"
    ]

    def parse(self, response):
        data = response.css("body > div > div > div > div")[3]
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
        item["referer"] = image

        yield item
        if next_page:
            next_url = "%s%s" % (self._BASE_URL, next_page)
            yield scrapy.Request(next_url, callback=self.parse_sub_page)
