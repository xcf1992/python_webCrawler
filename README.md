This web crawler is used to download pictures from 
xiurenwang: repo xiuRenOrg, which is not accessible in China
http://www.xiuren.org/
and
aitaotu: repo taotu, which is accessible in China
https://www.aitaotu.com/

Install:
pip install -r requirements.txt

Design:
Use Scrapy as the framework.

Usage:
Change start_urls from in taotu_spider.py or xiu_ren_spider.py under spiders repo,
the list of url is the page you want to start to download images;
For xiuren, the url should be like "http://www.xiuren.org/page-4.html", which is the index page
for different image collections.
For aitaotu, the url should be like https://www.aitaotu.com/tag/ttns.html, which is the index page
of different image collections or brands.

Make sure you have created /image repo under first level /taotu and /xiuRenOrg

After setting up everything you can run the crawler use:
scrapy crawl [xiu_re]|[taotu]
Then all the images will be downloaded automatically for you.

Reference:
https://docs.scrapy.org/en/latest/intro/tutorial.html