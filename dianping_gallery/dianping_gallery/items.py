# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Review(scrapy.Item):
	idx = scrapy.Field()
	shop = scrapy.Field()
	user_name = scrapy.Field()
	address = scrapy.Field()
	time = scrapy.Field()
	rate = scrapy.Field()
	content = scrapy.Field()
	image_urls  = scrapy.Field()