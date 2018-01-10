# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader.processors import TakeFirst


class ToystoresItem(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    category = scrapy.Field()
    description = scrapy.Field()
    specification = scrapy.Field()
    price = scrapy.Field(output_processor=TakeFirst())
    images = scrapy.Field()
    image_urls = scrapy.Field()
