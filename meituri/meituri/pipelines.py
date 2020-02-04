# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import urllib2
import traceback
import os
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


class MeituriPipeline(object):
    _BASE_REPO = "./image/"

    def process_item(self, item, spider):
        for index in range(0, len(item["names"])):
            image_name = self._BASE_REPO + item["names"][index].strip() + ".jpg"
            image_url = item["urls"][index].strip()
            if os.path.exists(image_name):
                print("Already exist, return directly")
                continue
            self.download_image(image_name, image_url)
        return item

    def download_image(self, img_name, img_url):
        with open(img_name, "w") as image:
            image.write(urllib2.urlopen(img_url).read())