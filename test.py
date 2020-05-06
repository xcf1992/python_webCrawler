import urllib.request
import traceback
import os
import sys
from importlib import reload
reload(sys)

def get_webpage(url, file_name):
    with open("file_name", "w") as image:
        image.write(urllib2.urlopen(url).read())

def download_image_1(image_url, image_name):
    with open(image_name, "wb") as image:
        #print(f"{urllib.request.urlopen(image_url).read()}")
        image.write(urllib.request.urlopen(image_url).read())

if __name__ == "__main__":
    test = "adfd/adsfadf/asdf".replace("/", "")
    print(f"{test}")
    #download_image_1("https://img.hywly.com/a/1/5474/1.jpg", "./test.jpg")
    #download_image_1("https://ii.hywly.com/a/1/26793/1.jpg", "./image/Manuela+ [HuaYan] Vol.047 6.jpg.jpg")