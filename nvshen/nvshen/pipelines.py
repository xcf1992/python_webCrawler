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


class NvshenPipeline(object):
    _BASE_REPO = "/Users/chenfu.xie/Work/python_webCrawler/nvshen/image/"

    def generate_url(self, url):
        remove_thumb = url.replace("/thumb_600x900", "")
        return f"https:{remove_thumb}"

    def process_item(self, item, spider):
        for index in range(0, len(item["names"])):
            origin_url = item["urls"][index].strip()
            image_name = self._BASE_REPO + item["names"][index].strip().replace("/", "") + ".jpg"
            if os.path.exists(image_name):
                print("Already exist, return directly")
                continue

            image_url = self.generate_url(origin_url)
            self.download_image(image_name, image_url)
        return item

    def download_image(self, img_name, img_url):
        headers = {
            'user-agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            'referer': 'https://www.xsnvshen.com/album/32697'
        }
        with open(img_name, "wb") as image:
            req = urllib.request.Request(img_url, headers=headers)
            con = urllib.request.urlopen(req)
            image.write(con.read())
