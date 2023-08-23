import scrapy
from selenium import webdriver
from scrapy import Selector
from scrapy.utils.project import get_project_settings
from scrapy_selenium import SeleniumRequest
from ..items import Product
import time


class ProductSpider(scrapy.Spider):
    name = "product"
    allowed_domains = ["shop.mango.com"]
    start_urls = ["https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99"]

    def parse(self, response, *args, **kwargs):
        driver = webdriver.Chrome()
        driver.get("https://shop.mango.com/bg-en/men/t-shirts-plain/100-linen-slim-fit-t-shirt_47095923.html?c=07")
        time.sleep(5)
        sel = Selector(text=driver.page_source)
        product = Product()
        product['name'] = "".join(sel.css('.product-name::text').extract())
        product['price'] = float("".join(sel.css('.sAobE::text').extract()).split(' ')[1])
        product['colour'] = "".join(sel.css('.colors-info-name::text').extract())
        product['size'] = sel.css('.gk2V5::text').extract()
        yield product

