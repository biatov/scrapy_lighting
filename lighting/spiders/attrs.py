import json

import scrapy
from scrapy import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pyvirtualdisplay import Display
from ..items import AttrsItem
import logging

logger = logging.getLogger('status scrape')


class Attrs(scrapy.Spider):
    name = 'info'
    allowed_domains = ['royallighting.com']
    start_urls = ['http://royallighting.com/']

    def __init__(self, **kwargs):
        super(Attrs).__init__(**kwargs)
        self.display = Display(visible=0, size=(1024, 768))
        self.display.start()
        self.driver = webdriver.Chrome()

    def parse(self, response):
        no_data = ''
        item = AttrsItem()
        try:
            with open('attrs.json') as f:
                data = json.load(f)
                attrs = map(lambda each: each['url'], data)
                try:
                    cat = list(map(lambda c: c['category'], data))[0]
                except IndexError:
                    cat = ''
        except:
            attrs = list()
            cat = ''
        url = 'http://royallighting.com/search_individual_result.asp?current='
        item['category'] = cat if cat else 'No Category'
        for attr in attrs:
            self.driver.get(''.join([url, attr]))
            try:
                element = WebDriverWait(self.driver, 5).until(
                    ec.presence_of_element_located((By.ID, "PHA4"))
                )
            except:
                pass
            selenium_response_text = self.driver.page_source
            response = Selector(text=selenium_response_text)
            try:
                item['title'] = response.xpath('//div[@id="productname"]/text()').extract_first().strip()
            except AttributeError:
                item['title'] = no_data
            item['id'] = attr
            price = response.xpath('//span[@id="XPRICEITEM"]/text()').extract_first()
            if not price:
                price = ', '.join(list(
                    filter(
                        None,
                        map(
                            lambda p: p.strip(),
                            response.xpath('//div[@class="product_sale left c_left"]/text()').extract()
                        )
                    )
                ))
            try:
                item['price'] = price.strip()
            except AttributeError:
                item['price'] = no_data
            try:
                item['reg_price'] = response.xpath(
                    '//div[@class="product_list left c_left"]/span/text()'
                ).extract_first().strip()
            except AttributeError:
                item['reg_price'] = no_data
            try:
                item['description'] = response.xpath('//div[@id="large_desc"]/text()').extract_first().strip()
            except AttributeError:
                item['description'] = no_data
            try:
                item['img'] = response.xpath('//img[@id="XIMGMAIN"]/@src').extract_first().strip()
            except AttributeError:
                item['img'] = no_data
            try:
                item['height'] = response.xpath(
                    '//td[contains(text(), "Height")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['height'] = no_data
            try:
                item['width'] = response.xpath(
                    '//td[contains(text(), "Width")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['width'] = no_data
            try:
                item['length'] = response.xpath(
                    '//td[contains(text(), "Length")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['length'] = no_data
            try:
                item['upc'] = response.xpath(
                    '//td[contains(text(), "UPC")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['upc'] = no_data
            try:
                item['instructions'] = response.xpath(
                    '//td[contains(text(), "Instructions")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['instructions'] = no_data
            try:
                item['parts_diagram'] = response.xpath(
                    '//td[contains(text(), "Parts Diagram")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['parts_diagram'] = no_data
            try:
                item['glass'] = response.xpath(
                    '//td[contains(text(), "Glass")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['glass'] = no_data
            try:
                item['safety_listing'] = response.xpath(
                    '//td[contains(text(), "Safety Listing")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['safety_listing'] = no_data
            try:
                item['weight'] = response.xpath(
                    '//td[contains(text(), "Weight")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['weight'] = no_data
            try:
                item['chain'] = response.xpath(
                    '//td[contains(text(), "Chain")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['chain'] = no_data
            try:
                item['wire'] = response.xpath(
                    '//td[contains(text(), "Wire")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['wire'] = no_data
            try:
                item['number_of_bulbs'] = response.xpath(
                    '//td[contains(text(), "Number of Bulbs")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['number_of_bulbs'] = no_data
            try:
                item['max_wattage'] = response.xpath(
                    '//td[contains(text(), "Max. Wattage")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['max_wattage'] = no_data
            try:
                item['bulb_base'] = response.xpath(
                    '//td[contains(text(), "Bulb Base")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['bulb_base'] = no_data
            try:
                item['light_sourse'] = response.xpath(
                    '//td[contains(text(), "Light Source")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['light_sourse'] = no_data
            try:
                item['dimmable'] = response.xpath(
                    '//td[contains(text(), "Dimmable")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['dimmable'] = no_data
            try:
                item['bulb_voltage'] = response.xpath(
                    '//td[contains(text(), "Bulb Voltage")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['bulb_voltage'] = no_data
            try:
                item['manufacturers_warranty'] = response.xpath(
                    '//td[contains(text(), "Manufacturer\'s Warranty")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['manufacturers_warranty'] = no_data
            finish = response.xpath(
                '//div[contains(text(), "Finish")]/following-sibling::div/text()'
            ).extract_first()
            if not finish:
                finish = response.xpath(
                    '//div[contains(text(), "Finish")]/following-sibling::div/select/option/text()'
                ).extract_first()
            try:
                item['finish'] = finish.strip()
            except AttributeError:
                item['finish'] = no_data

            try:
                item['extension'] = response.xpath(
                    '//td[contains(text(), "Extension")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['extension'] = no_data
            try:
                item['shipped_via'] = response.xpath(
                    '//td[contains(text(), "Shipped Via")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['shipped_via'] = no_data
            try:
                item['bulbs_included'] = response.xpath(
                    '//td[contains(text(), "Bulbs Included")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['bulbs_included'] = no_data
            try:
                item['bulb_type'] = response.xpath(
                    '//td[contains(text(), "Bulb Type")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['bulb_type'] = no_data
            try:
                item['color_temp'] = response.xpath(
                    '//td[contains(text(), "Color Temp")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['color_temp'] = no_data
            try:
                item['cri'] = response.xpath(
                    '//td[contains(text(), "CRI")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['cri'] = no_data
            try:
                item['light_output'] = response.xpath(
                    '//td[contains(text(), "Light Output")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['light_output'] = no_data
            try:
                item['rated_avg_life'] = response.xpath(
                    '//td[contains(text(), "Rated Avg. Life")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['rated_avg_life'] = no_data
            try:
                item['canopy'] = response.xpath(
                    '//td[contains(text(), "Canopy")]/following-sibling::td/text()'
                ).extract_first().strip()
            except AttributeError:
                item['canopy'] = no_data
            yield item
            logger.info('Scraped info from item with id=%s', attr)
        self.driver.close()
        self.display.stop()
