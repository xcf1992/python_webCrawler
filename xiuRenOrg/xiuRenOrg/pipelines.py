import os
import traceback
import urllib2


class XiurenorgPipeline(object):
    _RETRY_LIMIT = 3
    _BASE_REPO = "./image/"

    def process_item(self, item, spider):
        name = item["title"].split("-")[0]

        for link in item["img_link"]:
            image_name = name + "_" + link.split("/")[-1]
            self.save_image(self._BASE_REPO + image_name, link)

        return item

    def save_image(self, name, link):
        if os.path.exists(name):
            print "Already exist, return directly"
            return

        for i in range(self._RETRY_LIMIT):
            try:
                with open(name, "w") as image:
                    image.write(urllib2.urlopen(link).read())
                    break
            except Exception, e:
                if i < self._RETRY_LIMIT:
                    print '!Get exception: %s' % e
                    continue
                else:
                    print '!!!Failed to download image: %s' % link
                    traceback.print_exc()

        return
