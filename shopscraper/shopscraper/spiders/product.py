import scrapy
from selenium import webdriver
from scrapy import Selector
import time
from ..items import Product
import json


class ProductSpider(scrapy.Spider):
    name = "product"
    allowed_domains = ["shop.mango.com"]
    start_urls = ["https://shop.mango.com/bg-en/men/t-shirts-plain/100-linen-slim-fit-t-shirt_47095923.html?c=07"]
    headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US, en;q = 0.9",
            "Referer": "https://shop.mango.com/bg-en/men/t-shirts-plain/100-linen-slim-fit-t-shirt_47095923.html?c=07",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site" : "same-origin",
             "User-Agent" : "Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/116.0.0.0 Safari/537.36"
    }

    # driver = webdriver.Chrome() - UNMARK TO WORK WITH SELENIUM

    def start_requests(self):
        url = "https://shop.mango.com/services/garments/068/en/S/4709592307"
        request = scrapy.Request(url, callback=self.parse, headers=self.headers)
        yield request

    def parse(self, response, *args, **kwargs):
        raw_data = response.body
        data = json.loads(raw_data)
        product = Product()
        size = []
        product['name'] = data['name']
        for el in data['colors'].get('colors'):
            product['price'] = el['price']['price']
            product['colour'] = el['label']
            [size.append(item['value']) for item in el['sizes']]
            product['size'] = size
            break

        yield product

        # UNMARK BELOW TO RUN WITH SELENIUM

        # def parse(self, response, *args, **kwargs):
            # self.driver.get("".join(self.start_urls))
            # time.sleep(5)
            # sel = Selector(text=self.driver.page_source)
            # product = Product()
            # product['name'] = "".join(sel.css('.product-name::text').extract())
            # product['price'] = float("".join(sel.css('.sAobE::text').extract()).split(' ')[1])
            # product['colour'] = "".join(sel.css('.colors-info-name::text').extract())
            # product['size'] = sel.css('.gk2V5::text').extract()
            # yield product

