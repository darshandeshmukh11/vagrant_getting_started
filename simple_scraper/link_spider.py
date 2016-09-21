from scrapy.spiders import CrawlSpider, Rule
#from scrapy.linkextractors import LxmlLinkExtractor
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor

class someSpider(CrawlSpider):
  name = 'crawltest'
  allowed_domains = ['url']
  start_urls = ['url']

  rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse_obj', follow=True),)


  def parse_obj(self,response):
    for link in LxmlLinkExtractor(allow=(),deny = self.allowed_domains).extract_links(response):
        print link 
