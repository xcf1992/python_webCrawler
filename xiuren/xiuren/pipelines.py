# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request
import os
import sys
import wget
import random
import time
from datetime import datetime
from importlib import reload
reload(sys)


class XiurenPipeline(object):
    _BASE_REPO = "./image/"

    def process_item(self, item, spider):
        name = item["name"]
        print(f"[process_item] downloading {name}")

        for link in item["urls"]:
            image_name = self._BASE_REPO + name + "_" + link.split("/")[-1]
            # print(f"image name is {image_name}")
            if os.path.exists(image_name):
                print("Already exist, return directly")
                continue
            self.save_image(image_name, link)
        return item

    def save_image(self, name, link):
        print(f"[save_image] {datetime.now().strftime('%H:%M:%S')} {name}")
        ref = "http://www.xiuren.org/" + link.split("/")[-2] + ".html"
        headers = {
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
            'referer': ref,
            "connection": "keep-alive"
        }

        try:
            time.sleep(random.randint(2, 3))
            # wget.download(link, out=name)
            with open(name, "wb") as image:
                req = urllib.request.Request(link, headers=headers)
                con = urllib.request.urlopen(req)
                image.write(con.read())
        except Exception as e:
            print(f"failed link:{link}")
            print(f'Get exception: {e}')
