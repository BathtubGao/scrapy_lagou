import scrapy
from scrapy_lagou.jobItems import JobItem
from scrapy import Request
from scrapy import FormRequest
from scrapy_lagou.settings import *
import json

class LagouSpider(scrapy.Spider):
    # 设置name
    name = "lagou"
    # 设定域名
    allowed_domains = ["www.lagou.com"]
    # 填写爬取地址
    start_urls = ["http://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8D%97%E4%BA%AC&needAddtionalResult=false"]
    # POST请求表单数据
    # formdata = {
    #     'first': 'true',
    #     'pn': '1',
    #     'kd': 'Java'
    # }
    # 禁止重定向请求
    # meta = {
    #     'dont_redirect': True,
    #     'handle_httpstatus_list': [302]
    # }
    def start_requests(self):
        # 设置翻页次数
        for pn in range(1, 30):
            formdata = {
                'first': 'true',
                'pn': str(pn),
                'kd': 'Java'
            }
            print(formdata)
            # 带着cookie向网站服务器发请求，表明我们是一个已登录的用户
            yield FormRequest(self.start_urls[0], method='POST', callback=self.parse, formdata=formdata, cookies=COOKIES, headers=HEADER)

    def parse(self, response):
        res = json.loads(response.body.decode('utf-8'))
        for job in res['content']['positionResult']['result']:
            item = JobItem()
            item['company_full_name'] = job['companyFullName']
            item['company_short_name'] = job['companyShortName']
            item['position_id'] = job['positionId']
            item['position_url'] = 'https://www.lagou.com/jobs/' + str(job['positionId']) + '.html'
            # 通过meta传递item值
            yield Request(item['position_url'], meta={'item': item}, callback=self.parse_followers,
                          cookies=COOKIES, headers=HEADER)

    def parse_followers(self, response):
        item = response.meta['item']
        print(item)
        item['description'] = ''.join(response.xpath('//dd[@class="job_bt"]/div/p/text()').extract()).replace(u'\xa0', u'').strip()
        return item