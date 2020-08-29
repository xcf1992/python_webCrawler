# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request
import traceback
import os
import sys
import wget
from importlib import reload
reload(sys)


class XiurenPipeline(object):
    _BASE_REPO = "./image/"

    def process_item(self, item, spider):
        name = item["name"]
        print(f"[process_item] dowloading {name}")

        for link in item["urls"]:
            image_name = self._BASE_REPO + name + "_" + link.split("/")[-1]
            # print(f"image name is {image_name}")
            if os.path.exists(image_name):
                print("Already exist, return directly")
                continue
            self.save_image(image_name, link)
        return item

    def save_image(self, name, link):
        print(f"[save_image] {name}")
        headers = {
            'user-agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            'referer': 'http://www.xiuren.org/'
        }

        try:
            wget.download(link, out=name)
            #with open(name, "wb") as image:
                #req = urllib.request.Request(link, headers=headers)
                #con = urllib.request.urlopen(req)
                #image.write(con.read())
        except Exception as e:
            print(f"failed link:{link}")
            print(f'Get exception: {e}')
