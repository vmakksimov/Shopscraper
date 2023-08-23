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

    # def start_requests(self):
    #     # settings = get_project_settings()
    #     # driver_path = settings.get('CHROME_DRIVER_PATH')
    #     # driver = webdriver.Chrome(driver_path)
    #     url = "https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99"
    #     yield SeleniumRequest(url=url, callback=self.parse, wait_time=10)
        # driver.get(url)
        # time.sleep(
        #     5)
        # sel = Selector(text=driver.page_source)
        # name = sel.css('.product-name::text').extract()
        # price = sel.css('.sAobE ::text').extract()
        # yield scrapy.Request(name[0])
        # driver.quit()
        # item_ano = sel.xpath('//*[@class="product-name"]//text()').extract()  # It is also working

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

        # for li in sel.css('.knfzQ').extract():
        #     if li ==
        #             product['sizes'] = li

        # in_stock = sel.css('.ENYWg::text').extract()
        # if len(in_stock) > 0:


        yield product

