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
        headers = {
            'user-agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            'referer': 'https://www.xsnvshen.com/album/32697'
        }
        req = urllib.request.Request(image_url, headers=headers)
        con = urllib.request.urlopen( req )
        image.write(con.read())

if __name__ == "__main__":
    test = "adfd/adsfadf/asdf".replace("/", "")
    print(f"{test}")
    download_image_1("https://img.xsnvshen.com/album/24410/32697/001.jpg", "./test.jpg")
    #download_image_1("https://ii.hywly.com/a/1/26793/1.jpg", "./image/Manuela+ [HuaYan] Vol.047 6.jpg.jpg")