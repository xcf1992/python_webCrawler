# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import urllib.request
import traceback
import os
import sys
from importlib import reload
reload(sys)


class MeituriPipeline(object):
    _BASE_REPO = "/Users/chenfu.xie/Work/python_webCrawler/meituri/image/"

    def process_item(self, item, spider):
        for index in range(0, len(item["names"])):
            image_url = item["urls"][index].strip()
            image_name = self._BASE_REPO + item["names"][index].strip().replace("/", "") + ".jpg"
            # image_name = image_name.encode('ascii', errors='ignore')
            if os.path.exists(image_name):
                print("Already exist, return directly")
                continue
            self.download_image(image_name, image_url)
        return item

    def download_image(self, img_name, img_url):
        #print("name: " + img_name)
        with open(img_name, "wb") as image:
            image.write(urllib.request.urlopen(img_url).read())
