# -*- coding: utf-8 -*-

# Scrapy settings for youdaofanyi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'youdaofanyi'

SPIDER_MODULES = ['youdaofanyi.spiders']
NEWSPIDER_MODULE = 'youdaofanyi.spiders'
MONGODB_DBNAME = 'youdaofanyi'
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
COLLECTIONNAME = 'fanyi'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'youdaofanyi (+http://www.yourdomain.com)'
FILEPATH = '/home/xiyujing/文档/测试.txt'
HEADERS = {
    # 'Accept':  'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Encoding':  'gzip, deflate',
    # 'Accept-Language':  'zh-CN,zh;q=0.9',
    # 'Connection':  'keep-alive',
    # 'Content-Length':  '268',
    # 'Content-Type':  'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Host':  'fanyi.youdao.com',
    # 'Origin':  'http://fanyi.youdao.com',
    # 'Referer':  'http://fanyi.youdao.com/',
    'User-Agent':  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 'X-Requested-With':  'XMLHttpRequest',
}
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'youdaofanyi.middlewares.YoudaofanyiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'youdaofanyi.middlewares.YoudaofanyiDownloaderMiddleware': 543,
    'youdaofanyi.middlewares.HttpProxyMiddleware': 300,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'youdaofanyi.pipelines.YoudaofanyiPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
