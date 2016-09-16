# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
#
#Items are containers that will be loaded with the scraped data; they work like simple Python dicts

import scrapy


class SubPageItem(scrapy.Item):
    title = scrapy.Field()
    img_link = scrapy.Field()

class MainPageItem(scrapy.Item):
    subPage_link = scrapy.Field()
