# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest
import execjs
import pymysql
import json
from youdaofanyi.items import YoudaofanyiItem
from youdaofanyi import settings
from urllib import parse
import random
import logging
from twisted.internet.error import ConnectionRefusedError
class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    #allowed_domains = ['sss']
    #start_urls = ['http://fanyi.youdao.com']
    headers = settings.HEADERS
    filePath = settings.FILEPATH

    # def get_ts_and_salt(self):
    #     jsCode = """function tssalt() {
    #     var r = "" + (new Date).getTime(),i = r + parseInt(10 * Math.random(), 10);
    #     tssalt = {'ts': r, 'salt': i}
    #     return tssalt
    # }"""
    #     jsPlus = execjs.compile(jsCode)
    #     return jsPlus.call('tssalt',)

    def start_requests(self):
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        formdata = {
           # 'ts': self.get_ts_and_salt()['ts'],
           # 'salt': self.get_ts_and_salt()['salt'],
            'i':  '',
            'from':  'zh-CHS',
            'to':  'en',
            'smartresult':  'dict',
           # 'client':  'fanyideskweb',
           # 'salt':  '15470047624306',
           # 'sign':  '32086aa422da37fbef059aec2af34cc6',
            #'ts':  '1547004762430',
           # 'bv':  '59a2ee1b62619c43589e27bb52c2517a',
            'doctype':  'json',
            #'version':  '2.1',
            #'keyfrom':  'fanyi.web',
            #'action':  'FY_BY_REALTIME',
            #'typoResult':  'false',
        }
        with open(self.filePath, 'r') as f:
            kws = f.readlines()
        for kw in kws:
            keyword = kw.strip()
            formdata['i'] = keyword
            #从数据库获取代理
            yield FormRequest(url=url, callback=self.parse, formdata=formdata, headers=self.headers, meta={'tag': 0}, dont_filter=True)


    def parse(self, response):
        html = json.loads(response.text)
        #html = json.loads(requests.post(url=url, data=formdata, headers=self.headers).text)
        zhToen = html['translateResult'][0][0]
        item = YoudaofanyiItem()
        item['original'] = zhToen['src']
        item['translation'] = zhToen['tgt']
        yield item




