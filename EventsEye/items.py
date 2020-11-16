# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EventseyeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    section = scrapy.Field()
    cycle = scrapy.Field()
    date = scrapy.Field()
    city = scrapy.Field()
    venue = scrapy.Field()
    organiser = scrapy.Field()
    organiser_website = scrapy.Field()
    event_website = scrapy.Field()
    # eeye_link = scrapy.Field()