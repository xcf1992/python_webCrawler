# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib2
import traceback
import os
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


class XiurenorgPipeline(object):
    _RETRY_LIMIT = 3
    _BASE_REPO = "./image/"

    def process_item(self, item, spider):
        name = item["title"].split("-")[0]

        for link in item["img_link"]:
            image_name = name + "_" + link.split("/")[-1]
            self.save_image(self._BASE_REPO + image_name, link)
        return item

    def download_image(self, img_name, img_url):
        with open(img_name, "w") as image:
            image.write(urllib2.urlopen(img_url).read())

    def save_image(self, name, link):
        if os.path.exists(name):
            print "Already exist, return directly"
            return

        for i in range(self._RETRY_LIMIT):
            try:
                self.download_image(name, link)
                break
            except Exception, e:
                if i < self._RETRY_LIMIT:
                    print '!Get exception: %s' % e
                    continue
                else:
                    print '!!!Failed to download image: %s' % link
                    traceback.print_exc()

        return
