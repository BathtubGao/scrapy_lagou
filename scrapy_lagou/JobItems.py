import scrapy

class JobItem(scrapy.Item):
    # 跳转地址
    position_link = scrapy.Field()