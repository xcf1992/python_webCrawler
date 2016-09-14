import urllib2


def get_page():
    try:
        request = urllib2.Request("http://www.xiuren.org/")
        #request = urllib2.Request("http://www.xiuren.org/mistar-056.html")
        #request = urllib2.Request("http://www.xiuren.org/mistar/056/0012.jpg")
        response = urllib2.urlopen(request)
        print response.read()
    except urllib2.URLError, exc:
        print exc.reason


if __name__ == "__main__":
    get_page()