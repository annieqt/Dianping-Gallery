# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Review(scrapy.Item):
	name = scrapy.Field()
	title = scrapy.Field()
	address = scrapy.Field()
	time = scrapy.Field()
	rate = scrapy.Field()
	content = scrapy.Field()
	file_urls = scrapy.Field()
