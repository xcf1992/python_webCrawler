This web crawler is used to download pictures from different webs

# Install:
pip install -r requirements.txt

# Design:
Use Scrapy as the framework.

# Usage:
Change start_urls from in taotu_spider.py or xiu_ren_spider.py under spiders repo,
the list of url is the page you want to start to download images;  
Make sure you have created /image repo under first level /taotu and /xiuRenOrg

## XiuRen
For xiuren, the url should be like "http://www.xiuren.org/page-4.html", which is the index page
for different image collections.
```
scrapy crawl xiuren | grep save_image > download.log
```
This step will get all image name and link to download.log
```
python downloader.py
```
This step will download the actual image from the links in the download.log

## nvshen
Base web is www.xsnvshen.com, this web limit access rate
TODO: adjust access rate
```
scrapy crawl nvshen | grep save_image > download.log
```

## tujigu
Base web is tujigu.com. The collections here is not complete.  
```scrapy crawl tujigu | grep save_image > download.log```

## AiTaoTu
For aitaotu, the url should be like https://www.aitaotu.com/tag/ttns.html, which is the index page
of different image collections or brands.

## meituri
This web has been deprecated.

# Reference:
https://docs.scrapy.org/en/latest/intro/tutorial.html