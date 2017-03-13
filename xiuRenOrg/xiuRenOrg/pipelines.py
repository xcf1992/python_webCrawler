import os
import urllib2

class XiurenorgPipeline(object):
    def process_item(self, item, spider):
        name = item["title"].split("-")[0]
        directory = "./image/"
        
        for link in item["img_link"]:
            image_name = name + "_" + link.split("/")[-1]
            with open(directory + "/" + image_name, "w") as image:
                image.write(urllib2.urlopen(link).read())

        return item
