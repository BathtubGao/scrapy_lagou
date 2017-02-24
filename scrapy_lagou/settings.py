# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_lagou project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_lagou'

SPIDER_MODULES = ['scrapy_lagou.spiders']
NEWSPIDER_MODULE = 'scrapy_lagou.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_lagou (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapy_lagou.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy_lagou.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scrapy_lagou.savePipeline.SavePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

HEADER = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'www.lagou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
}

COOKIES = {
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
