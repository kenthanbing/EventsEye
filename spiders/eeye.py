# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from EventsEye.items import EventseyeItem


class EeyeSpider(CrawlSpider):
    name = 'eeye'
    allowed_domains = ['eventseye.com']
    country = input('Enter a country name:')
    start_urls = [f'https://www.eventseye.com/fairs/c1_trade-shows_{country}.html']

    rules = (
        Rule(LinkExtractor(allow=(f'shows_{country}_\d+\.html', f'shows_{country}\.html')), follow=True),

        #获取详情页信息
        Rule(LinkExtractor(allow='fairs/f'), callback='parse_item', follow=False)
        )
    def parse_item(self, response):
        item = EventseyeItem()
        item['name'] = response.css('.title-line h1::text').extract_first().strip()
        item['section'] = response.xpath('/html/body/div[5]/div[1]/text()').extract()[1].strip()
        item['cycle'] = response.xpath('/html/body/div[5]/div[3]/div[2]/text()').extract()[1].strip()
        item['date'] = response.css('.dates td::text').extract_first().strip()
        try:
            item['city'] = response.css('.dates a::text').extract_first().strip()
        except:
            item['city'] = ''
        item['venue'] = response.css('.dates td+td+td::text').extract_first().strip()
        item['organiser'] = response.css('.orglink::text').extract_first().strip()
        item['organiser_website'] = response.xpath('//a[@class="ev-web"]/@href').extract()[0].strip()
        item['event_website'] = response.xpath('/html/body/div[9]/div[1]/a[1]/@href').extract()[0].strip()
        item['eeye_link'] = response.xpath('/html/head/link[3]/@href').extract()[0].strip()

        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
