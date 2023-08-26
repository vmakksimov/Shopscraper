import scrapy
from selenium import webdriver
from scrapy import Selector
import time
import json


class ProductSpider(scrapy.Spider):
    name = "product"
    allowed_domains = ["shop.mango.com"]
    start_urls = ["https://shop.mango.com/bg-en/men/t-shirts-plain/100-linen-slim-fit-t-shirt_47095923.html?c=07"]
    driver = webdriver.Chrome()

    def parse(self, response, *args, **kwargs):
        self.driver.get("".join(self.start_urls))
        time.sleep(5)
        sel = Selector(text=self.driver.page_source)
        yield {
            'name': "".join(sel.css('.product-name::text').extract()),
            'price': float("".join(sel.css('.sAobE::text').extract()).split(' ')[1]),
            'colour': "".join(sel.css('.colors-info-name::text').extract()),
            'size': sel.css('.gk2V5::text').extract()
        }

    # UNMARK TO RUN WITH SCRAPY ONLY

    # def start_requests(self):
    #     url = "https://shop.mango.com/services/garments/068/en/S/4709592307"
    #     request = scrapy.Request(url, callback=self.parse)
    #     yield request
    #
    # def parse(self, response, *args, **kwargs):
    #     raw_data = response.body
    #     data = json.loads(raw_data)
    #     name = data['name']
    #     size = []
    #     price = ''
    #     colour = ''
    #     for el in data['colors'].get('colors'):
    #         price = el['price']['price']
    #         colour = el['label']
    #         [size.append(item['value']) for item in el['sizes']]
    #         break
    #
    #     yield {
    #         'name' : name,
    #         'price' : price,
    #         'colour' : colour,
    #         'size' : size
    #     }




