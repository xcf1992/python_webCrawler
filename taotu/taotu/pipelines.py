# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib2


class TaotuPipeline(object):
    _BASE_REPO = "./image/"

    def process_item(self, item, spider):
        title = item["title"].split("-")[0].strip()

        for link in item["image"]:
            image_name = "%s_%s" % (title, link.split("/")[-1])
            with open(self._BASE_REPO + image_name, "w") as image:
                image.write(urllib2.urlopen(link).read())
        return item
