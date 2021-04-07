# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib.request
import os
import sys
from datetime import datetime
from importlib import reload
reload(sys)


class TujiguPipeline:
    _BASE_REPO = "/Users/chenfu.xie/Work/python_webCrawler/tujigu/image/"

    def process_item(self, item, spider):
        for idx in range(0, len(item["names"])):
            image_url = item["urls"][idx].strip()
            image_name = self._BASE_REPO + item["names"][idx].strip().replace("/", "") + ".jpg"
            if os.path.exists(image_name):
                print("Already exist, return directly")
                continue

            self.download_image_log(image_name, image_url)
        return item

    def download_image_log(self, img_name, img_url):
        print(f"[save_image_name] {datetime.now().strftime('%H:%M:%S')} {img_name}")
        print(f"[save_image_link] {datetime.now().strftime('%H:%M:%S')} {img_url}")