import scrapy
from scrapy_lagou.JobItems import JobItem
from scrapy import Request
from scrapy import FormRequest
import json

class LagouSpider(scrapy.Spider):
    # 设置name
    name = "LagouSpider"
    # 设定域名
    allowed_domains = ["lagou.com"]
    # 填写爬取地址
    start_urls = ["https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8D%97%E4%BA%AC&needAddtionalResult=false"]
    # http头
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '23',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_Java?px=default&city=%E5%8D%97%E4%BA%AC',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'
    }
    # cookie
    cookies = {
        'user_trace_token': '20161209173120-4094da5e20d84edd81a2c121b5d5f04d',
        'LGUID': '20161209173121-3ec9dc03-bdf2-11e6-bbe7-5254005c3644',
        'showExpriedIndex': '1',
        'showExpriedCompanyHome': '1',
        'showExpriedMyPublish': '1',
        'hasDeliver': '71',
        '_gat': '1',
        'index_location_city': '%E5%85%A8%E5%9B%BD',
        'PRE_HOST': 'www.baidu.com',
        'PRE_SITE': 'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D0Gnc-HmFdGHGrixovAgkuDVf0b4ekVcumvzDhDBXBtTkTsKVYL-pIIZ6-F7V7vAc%26wd%3D%26eqid%3Dd415978e000314570000000558a66a7c',
        'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2Fgongsi%2F34683.html',
        'login': 'false',
        'unick': "",
        '_putrc': "",
        'JSESSIONID': '3830F57AFADAD9B0654AA826433FA7BF',
        'TG-TRACK-CODE': 'search_code',
        '_ga': 'GA1.2.265869673.1481275878',
        'LGSID': '20170217161957-de1c2e65-f4e9-11e6-b568-525400f775ce',
        'LGRID': '20170217112144-357783ac-f4c0-11e6-b4c6-525400f775ce',
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1486690793,1486953439,1487138540,1487301262',
        'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1487301703',
        'SEARCH_ID': 'c12a4334955941a097b6a167faf3d488'
    }

    # POST请求表单数据
    formdata = {
        'first': 'true',
        'pn': '1',
        'kd': 'Java'
    }

    meta = {
        'dont_redirect': True,
        'handle_httpstatus_list': [302]
    }

    def start_requests(self):
        # 带着cookie向网站服务器发请求，表明我们是一个已登录的用户
        return [FormRequest(self.start_urls[0], method='POST', formdata=self.formdata, callback=self.parse,
                        meta=self.meta, cookies=self.cookies, headers=self.headers)]

    def parse(self, response):
        print('###########################')
        sites = json.loads(response.body.decode('gbk').encode('utf-8'))
        print(sites)
