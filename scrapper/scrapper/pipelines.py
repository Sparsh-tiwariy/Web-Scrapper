# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


# pymongo imported for connection of MongoDB server with python
import pymongo


class ScrapperPipeline(object):

    # This is the initialization function. This method __init__  acts like a constructor in python. This function will try to connect our mongo db database
    # And the parameter self is the instance of the object.

    def __init__(self):
        self.conn = pymongo.MongoClient('mongodb+srv://Sparsh123:Invoker7!@cluster0.7noqi.mongodb.net/test'
                                        )       # Connection String to the Database

        # A database is created by this named as "Sparsh_T" and inside it a collection is also created named as "flipkart".
        db = self.conn['Sparsh_T']
        self.collection = db['flipkart']

    # This is a process item method is automatically called and the parameter item will contain our all scraped data.
    def process_item(self, item, spider):
        # It inserts the scraped data in the dictionary format in our database.
        self.collection.insert_one(dict(item))
        return item
