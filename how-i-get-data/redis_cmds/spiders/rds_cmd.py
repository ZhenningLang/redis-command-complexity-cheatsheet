# -*- coding: utf-8 -*-

import re

import scrapy
from scrapy.http import Request, HtmlResponse


CSV_OUTPUT_FILE = open('output.csv', 'w')


def find_time_complexity_text(str_):
    cnt = 1  # push 1 '(' into brace stack
    start_idx = 2  # jump over O(
    for idx in range(start_idx, len(str_)):
        if str_[idx] == '(':
            cnt += 1
        elif str_[idx] == ')':
            cnt -= 1
            if cnt == 0:
                return str_[:idx + 1]
    return re.search(r'O\(.*?\)', str_).group(0)


# noinspection PyMethodMayBeStatic
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
                # noinspection PyBroadException
                try:
                    hint_idx = str(time_complexity_raw).find('O(')
                    time_complexity = find_time_complexity_text(time_complexity_raw[hint_idx:])
                except:  # noqa
                    time_complexity = response.url
        print(f'{cmd_group},[{cmd_name}]({response.url}),{time_complexity}')
        CSV_OUTPUT_FILE.write(f'{cmd_group},[{cmd_name}]({response.url}),{time_complexity}\n')
