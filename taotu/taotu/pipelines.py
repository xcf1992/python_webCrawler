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


class TaotuPipeline(object):
    _BASE_REPO = "./xixiwang/"
    _RETRY_LIMIT = 3

    def process_item(self, item, spider):
        title = item["title"].split("-")[0].strip()
        referer = item["referer"]

        for img_url in item["image"]:
            image_name = "%s_%s" % (title, img_url.split("/")[-1])
            self.save_image(self._BASE_REPO + image_name.strip(), referer, img_url)

        return item

    def download_image(self, img_name, referer, img_url):
        command = "wget -d --header='Referer: %s' %s --output-document='%s'" % (referer, img_url, img_name)
        os.system(command)

    def save_image(self, name, referer, img_url):
        if os.path.exists(name):
            print "Already exist, return directly"
            return

        for i in range(self._RETRY_LIMIT):
            try:
                self.download_image(name, referer[0], img_url)
            except Exception, e:
                if i < self._RETRY_LIMIT:
                    print '!Get exception: %s' % e
                    continue
                else:
                    print '!!!Failed to download image: %s' % img_url
                    traceback.print_exc()

        return
