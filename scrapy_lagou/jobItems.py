import scrapy

class JobItem(scrapy.Item):
    # 跳转ID
    position_id = scrapy.Field()
    # 跳转url
    position_url = scrapy.Field()
    # 公司全称
    company_full_name = scrapy.Field()
    # 公司简称
    company_short_name = scrapy.Field()
    # 职务描述
    description = scrapy.Field()
