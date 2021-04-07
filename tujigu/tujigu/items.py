# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TujiguItem(scrapy.Item):
    urls = scrapy.Field()
    names = scrapy.Field()
