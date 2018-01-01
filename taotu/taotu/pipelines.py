# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib2
import traceback
import os


class TaotuPipeline(object):
    _BASE_REPO = "./youmihui/"
    _RETRY_LIMIT = 3

    def process_item(self, item, spider):
        title = item["title"].split("-")[0].strip()

        for link in item["image"]:
            image_name = "%s_%s" % (title, link.split("/")[-1])
            self.save_image(self._BASE_REPO + image_name.strip(), link)

        return item

    def save_image(self, name, link):
        if os.path.exists(name):
            print "Already exist, return directly"
            return

        for i in range(self._RETRY_LIMIT):
            try:
                with open(name, "w") as image:
                    image.write(urllib2.urlopen(link).read())
                    break
            except Exception, e:
                if i < self._RETRY_LIMIT:
                    print '!Get exception: %s' % e
                    continue
                else:
                    print '!!!Failed to download image: %s' % link
                    traceback.print_exc()

        return
