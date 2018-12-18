# -*- coding: utf-8 -*-
import scrapy
from carproject.items import CarprojectItem
from scrapy.pipelines.images import ImagesPipeline
class BaomaSpider(scrapy.Spider):
    name = 'baoma'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html#pvareaid=3454438']

    def parse(self, response):
         fenleis=response.xpath("//div[@class='uibox']")[1:]
         for fenlei in fenleis:
             title=fenlei.xpath(".//div[@class='uibox-title']/a/text()").get()
             print(title)
             urls=fenlei.xpath(".//ul/li//img/@src").getall()
             urls=list(map(lambda x:response.urljoin(x),urls))
             item=CarprojectItem(fenlei=title,image_urls=urls)

             print(urls)
             yield item


