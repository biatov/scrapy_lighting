# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LightingItem(scrapy.Item):
    url = scrapy.Field()
    category = scrapy.Field()


class AttrsItem(scrapy.Item):
    title = scrapy.Field()
    id = scrapy.Field()
    category = scrapy.Field()
    reg_price = scrapy.Field()
    price = scrapy.Field()
    img = scrapy.Field()
    description = scrapy.Field()
    height = scrapy.Field()
    width = scrapy.Field()
    length = scrapy.Field()
    glass = scrapy.Field()
    safety_listing = scrapy.Field()
    weight = scrapy.Field()
    chain = scrapy.Field()
    wire = scrapy.Field()
    number_of_bulbs = scrapy.Field()
    max_wattage = scrapy.Field()
    bulb_base = scrapy.Field()
    light_sourse = scrapy.Field()
    dimmable = scrapy.Field()
    bulb_voltage = scrapy.Field()
    manufacturers_warranty = scrapy.Field()
    finish = scrapy.Field()
    upc = scrapy.Field()
    instructions = scrapy.Field()
    parts_diagram = scrapy.Field()

    extension = scrapy.Field()
    shipped_via = scrapy.Field()
    bulbs_included = scrapy.Field()
    bulb_type = scrapy.Field()
    color_temp = scrapy.Field()
    cri = scrapy.Field()
    light_output = scrapy.Field()
    rated_avg_life = scrapy.Field()
    canopy = scrapy.Field()
