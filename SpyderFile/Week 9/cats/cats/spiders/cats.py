# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 11:22:40 2018

@author: Lenovo
"""
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "cats"

    def start_requests(self):
        url = 'https://en.wikipedia.org/wiki/List_of_cat_breeds'

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'cats.html' 
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
