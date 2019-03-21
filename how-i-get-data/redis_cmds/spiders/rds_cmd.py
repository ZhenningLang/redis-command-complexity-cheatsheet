# -*- coding: utf-8 -*-

import re

import scrapy
from scrapy.http import Request, HtmlResponse


TIME_COMPLEXITY_PATTERN = re.compile(r'O\(.*?\)')


class RdsCmdSpider(scrapy.Spider):
    name = 'rds_cmd'
    allowed_domains = ['redis.io']
    start_urls = ['https://redis.io/commands', ]

    def parse(self, response: HtmlResponse):
        li_eles = response.selector.css('.container li')
        for ele in li_eles:
            cmd_group = ele.attrib['data-group']
            cmd_name = ele.attrib['data-name']
            detail_url = ele.css('a').attrib['href']
            yield Request(
                response.urljoin(detail_url),
                callback=self.parse_details,
                meta={'cmd_group': cmd_group, 'cmd_name': cmd_name}
            )

    def parse_details(self, response: HtmlResponse):
        cmd_group = response.meta['cmd_group']
        cmd_name = response.meta['cmd_name']
        meta_eles = response.selector.css('.metadata p')
        cnt = 1
        time_complexity = 'None'
        for ele in meta_eles:
            if cnt == 1:
                cnt += 1
            else:
                time_complexity_raw = ele.get()
                try:
                    time_complexity = re.search(TIME_COMPLEXITY_PATTERN, time_complexity_raw).group(0)
                except:
                    time_complexity = response.url
        print(f'{cmd_group},{cmd_name},{time_complexity}')
