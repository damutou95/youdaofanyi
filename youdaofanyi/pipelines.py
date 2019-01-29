# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from youdaofanyi import settings

class YoudaofanyiPipeline(object):

    def __init__(self):
        port = settings.MONGODB_PORT
        host = settings.MONGODB_HOST
        dbname = settings.MONGODB_DBNAME
        colname = settings.COLLECTIONNAME
        client = pymongo.MongoClient(host=host, port=port)
        mgd = client[dbname]
        self.post = mgd[colname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
