# -*- coding: utf-8 -*-

import scrapy

class VolSpider(scrapy.Spider):
    name = 'volleyball'
    
    start_urls = [
        'http://www.funtable.ru/table/sport/vse-chempiony-sssr-sng-i-rossii-po-voleybolu-muzhchiny.html'
    ]

    def parse(self, response):
        SET_SELECTOR='//*[@class="catalog-item-desc-float itemFullText"]//table/tbody/tr'
        for i in response.xpath(SET_SELECTOR):
            yield {
                'date': i.xpath('td[1]//text()').extract_first(default='').replace('\r', '').replace('\n', '').replace('\t', ''),
                'first': i.xpath('td[2]//text()').extract_first(default='').replace('\r', '').replace('\n', '').replace('\t', ''),
                'second': i.xpath('td[3]//text()').extract_first(default='').replace('\r', '').replace('\n', '').replace('\t', ''),
                'third': i.xpath('td[4]//text()').extract_first(default='').replace('\r', '').replace('\n', '').replace('\t', ''),
            }