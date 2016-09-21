import urllib2
import re

website = urllib2.urlopen('url')
html = website.read()
links = re.findall('"((http|ftp)s?://.*?)"', html)
for i, val in enumerate(links):
    print val