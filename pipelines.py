# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from .spiders.eeye import EeyeSpider

from scrapy import Item
import pymongo
class EventseyePipeline(object):
    """
    将item写入MongoDB
    """

    @classmethod
    def from_crawler(cls, crawler):
        cls.DB_URL = crawler.settings.get('MONGO_DB_URI', 'mongodb://localhost:27017')
        cls.DB_NAME = crawler.settings.get('MONGO_DB_NAME', 'scrapy_data')
        return cls()

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.DB_URL)
        self.db = self.client[self.DB_NAME]

    def process_item(self, item, spider):
        collection = self.db[f'{EeyeSpider.country}']
        post = dict(item) if isinstance(item, Item) else item
        collection.insert_one(post)
        return item

    def close_spider(self, spider):
        self.client.close()

