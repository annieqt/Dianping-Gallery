
import scrapy
# -*- coding: utf-8 -*-
from  scrapy.pipelines.images import ImagesPipeline
import os, os.path
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ReviewImagesPipeline(ImagesPipeline):
	def item_completed(self, results, item, info):
		shop = item['shop']
		user_name = item['user_name']		
		print("Finish downloading Review & Photos by user:", user_name, "at shop:", shop)
		for result in [x for ok, x in results if ok]:
			path = result['path']
			settings = get_project_settings()
			storage = settings.get('IMAGES_STORE')
			target_path = os.path.join(storage, user_name, shop, os.path.basename(path))
			path = os.path.join(storage, path)
			if not os.path.exists(os.path.join(storage, user_name, shop)):
				os.makedirs(os.path.join(storage, user_name, shop))
			os.rename(path, target_path)

			# if not os.rename(path, target_path):
			# 	print("if2:")
			# 	raise DropItem("Could not move image to target folder")

		if self.IMAGES_RESULT_FIELD in item.fields:
			item[self.IMAGES_RESULT_FIELD] = [x for ok, x in results if ok]
		return item			