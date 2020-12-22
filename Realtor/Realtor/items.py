
import scrapy


class RealtorItem(scrapy.Item):

    price=scrapy.Field()
    item_type=scrapy.Field()
    bedroom=scrapy.Field()
    bathroom=scrapy.Field()
    area=scrapy.Field()
    area_lot=scrapy.Field()
    address=scrapy.Field()
    school_data=scrapy.Field()
    neighborhood=scrapy.Field()
    city=scrapy.Field()
    neighborhood_data=scrapy.Field()
    nearby_neighborhoods_data=scrapy.Field()