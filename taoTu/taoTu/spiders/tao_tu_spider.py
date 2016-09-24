import scrapy
import os

class xiu_ren_spider(scrapy.Spider):
    name = "tao_tu"
    allowed_domains = ["aitaotu.com"]

    start_urls = ["http://www.aitaotu.com/tag/tuinvlang.html"]

    def parse(self, response):
        url_set = []
        with open("./urls", "r") as urls:
            for url in urls:
                url_set.append(url)

        for href in response.css("ul")[2].css("a"):
            print "-=-=-=-=-=-=-=-"
            print href.extract()
            print "-=-=-=-=-=-=-=-"
            return
            url = response.urljoin(href.extract())
            output = open("urls", "w")
            if url not in url_set:
                output.write(url + "\n")

            output.close()
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
