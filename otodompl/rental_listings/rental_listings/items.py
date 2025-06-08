# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Listings(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Id = scrapy.Field()
    Url = scrapy.Field()
    Title = scrapy.Field()
    Monthly_Cost = scrapy.Field()
    Location = scrapy.Field()
    Surface_Area = scrapy.Field()
    Rooms = scrapy.Field()
    Heating  = scrapy.Field()
    Floor_Number  = scrapy.Field()
    Condition =  scrapy.Field()
    Availabitiy_Date = scrapy.Field()
    Operational_Cost = scrapy.Field()
    Deposit = scrapy.Field()
    Type_of_Advertiser = scrapy.Field()
    '''
    Amenities = scrapy.Field()
    Building_Construction_Year = scrapy.Field()
    Lift = scrapy.Field()
    Type_of_Building = scrapy.Field()
    Windows = scrapy.Field()
    Security =  scrapy.Field()
    Additional_Features = scrapy.Field()
    Description = scrapy.Field()

    '''
