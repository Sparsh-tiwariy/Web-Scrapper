# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapperItem(scrapy.Item):

    # declaration the fields for the item used in the spider.
    brand = scrapy.Field()
    name = scrapy.Field()
    original_price = scrapy.Field()
    sale_price = scrapy.Field()
    image_url = scrapy.Field()
    product_page_url = scrapy.Field()
    product_category = scrapy.Field()
