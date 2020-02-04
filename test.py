import urllib2
import traceback
import os
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

def get_webpage(url, file_name):
    with open("file_name", "w") as image:
        image.write(urllib2.urlopen(url).read())

def download_image_1(image_url, image_name):
    with open(image_name, "w") as image:
        image.write(urllib2.urlopen(image_url).read())

if __name__ == "__main__":
    download_image_1("https://ii.hywly.com/a/1/31611/6.jpg", "./test.jpg")