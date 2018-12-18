# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from carproject import settings
import os
class CarprojectPipeline(object):
    def process_item(self, item, spider):
        return item
class myimagejectPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        requestdata=super(myimagejectPipeline, self).get_media_requests(item,info)
        for reqobj in requestdata:
               reqobj.item=item
        return requestdata
    def file_path(self, request, response=None, info=None):
        path=super(myimagejectPipeline, self).file_path(request,response,info)
        feilei=request.item.get("fenlei")
        imagesfile=settings.IMAGES_STORE
        feileimu= os.path.join(imagesfile,feilei)
        if not os.path.exists(feileimu):
            os.mkdir(feileimu)
        filename=path.replace("full/","")
        print(filename)
        print("*"*50)
        filepath=os.path.join(feileimu,filename)
        print(filepath)
        print("*" * 50)
        return filepath