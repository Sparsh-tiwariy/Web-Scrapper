# Important packages needed
from tracemalloc import start
from unicodedata import category
from ..items import ScrapperItem
import scrapy


def conversion(s):
    # This is the function to convert both original price and sale price from string to floating point number
    s = s.replace("$", "")
    s = s.replace(",", "")
    return float(s)


class FirstSpider(scrapy.Spider):       # The subclass of the spider
    name = 'scrapper'             # Name of the Scrapper

    # function for returning iterable of Requests which the spider will crawl from
    def start_requests(self):

        urls = [

            # URLs used for scraping
            'https://www.net-a-porter.com/en-in/shop/clothing/tops?pageNumber={}',
            'https://www.net-a-porter.com/en-in/shop/shoes?pageNumber={}'
        ]

        # loop used for iterating through multiple pages in URLs(pagination)
        for url in urls:
            # range of pages that is 25 pages.
            for i in range(0, 26):
                x = url.format(i)
                yield scrapy.Request(url=x, callback=self.parse)

    # It is the method for handling each of requests and process the response then returns scraped data
    def parse(self, response):

        # An instance variable of the class declared in items.py so that we can use this as a blueprint to store some items inside this items instance.
        items = ScrapperItem()

        # all_cards is a variable which contains the source code of this given tag only ; instead of whole page's source code. This class data was not needed, only items inside it was needed so get function is not used here.
        all_cards = response.css('.ProductListWithLoadMore52__listingGrid a')

        # loop to get the values one by one in a sequence instead of whole data at once.
        for products in all_cards:
            # css selector for extracting all the product names
            name = products.css('.ProductItem24__name::text').get()
            # css selector for extracting all the brand names of products
            brand = products.css('.ProductItem24__designer::text').get()
            original_price = products.css(
                '.PriceWithSchema9__value span::text').get()  # css selector for extracting original prices of all the products
            sale_price = products.css(
                '.PriceWithSchema9__value span::text').get()  # css selector for extracting sale prices of all the products
            image_url = products.css(
                '.Image18__imageContainer img::attr(src)').get()  # css selector for extracting image url of all the products
            product_page_url = products.css(
                'a::attr(href)').get()  # css selector for extracting product page url of all products
            type = response.css(
                '.ProductListWithLoadMore52__listingGrid meta::attr(content)').get()  # css selector for showing the product category of the products

            # Conversion of string to float of prices
            original_price = [conversion(price) for price in original_price]
            sale_price = [conversion(price) for price in sale_price]

            # conditional statements to show the product category of the products
            if "tops" in type:
                product_category = "Topwear"
            else:
                product_category = "Footwear"

            # It is storing all the extracted values inside an individual temporary item container in a proper format
            # The field name should be same as declared in items.py file.
            items['brand'] = brand
            items['name'] = name
            items['original_price'] = original_price
            items['sale_price'] = sale_price
            items['image_url'] = image_url
            items['product_page_url'] = product_page_url
            items['product_category'] = product_category

            # It is for returning our items that is our final output
            yield items
