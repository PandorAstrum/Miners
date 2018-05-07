# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GeneralscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    companyName = scrapy.Field()
    companySize = scrapy.Field()
    phoneNumber = scrapy.Field()
    position = scrapy.Field()
    address = scrapy.Field()
    domainName = scrapy.Field()
    peopleFirstName = scrapy.Field()
    peopleLastName = scrapy.Field()
    email = scrapy.Field()




