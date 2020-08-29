import urllib.request
import time
import os
import wget
import sys
import signal
from importlib import reload
reload(sys)


def download_image_1(image_url, image_name):
    with open(image_name, "wb") as image:
        # print(f"{urllib.request.urlopen(image_url).read()}")
        headers = {
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            'referer': 'https://www.xsnvshen.com/album/32697'
        }
        req = urllib.request.Request(image_url, headers=headers)
        con = urllib.request.urlopen( req )
        image.write(con.read())


def download_image_2(image_url, image_name):
    signal.alarm(5)
    try:
        wget.download(image_url, out=image_name)
    except TimeoutException:
        print(f"get hang when download [link]: {image_url}")
        print(f"get hang when download [name]: {image_name}")
    else:
        signal.alarm(0)


def get_name_and_link():
    names = []
    links = []
    with open("download.log", "r") as log:
        for data in log:
            line = data.strip()
            if line.startswith("[save_image_link]"):
                links.append(line[27:])
            if line.startswith("[save_image_name]"):
                names.append(line[27:])
    return names, links


def download_file():
    names, links = get_name_and_link()
    if len(names) != len(links):
        print(f"len names {len(names)} not equal to len links {len(links)}")
        return
    for i in range(0, len(names)):
        if os.path.exists(names[i]):
            print("Already exist, return directly")
            continue
        time.sleep(1)
        download_image_2(links[i], names[i])


def timeout_handler(signum, frame):   # Custom signal handler
    raise TimeoutException


class TimeoutException(Exception):   # Custom exception class
    pass


if __name__ == "__main__":
    # download_image_1("https://img.xsnvshen.com/album/24410/32697/001.jpg", "./test.jpg")
    # download_image_2("http://www.xiuren.org/xiuren2/XiuRen-N02016/0108.jpg", "./test.jpg")
    download_file()
