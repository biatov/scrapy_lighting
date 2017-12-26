import re

import scrapy
from scrapy import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
from ..items import LightingItem
import logging

logger = logging.getLogger('status check pages')


class Main(scrapy.Spider):
    name = 'main'
    allowed_domains = ['royallighting.com']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kwargs = kwargs
        if not kwargs:
            start_urls = ["http://royallighting.com/search_result.asp?params=Installation:1;"]
        else:
            params = list()

            def get_attr(attribute):
                value = kwargs.get(attribute, '')
                if value:
                    return ':'.join([attribute.capitalize(), value])
                return False

            all_data = ['installation', 'description', 'style', 'width', 'options', 'brand', 'finish']

            for each in all_data:
                check = get_attr(each)
                if check:
                    params.append(check)

            new_kwargs = ';'.join(params)
            start_urls = [
                "http://royallighting.com/search_result.asp?params={kw};".format(kw=new_kwargs)
            ]
        self.start_urls = start_urls
        self.display = Display(visible=0, size=(1024, 768))
        self.display.start()
        self.driver = webdriver.Chrome()

    def parse(self, response):
        item = LightingItem()
        if not self.kwargs:
            log_url = 'http://royallighting.com/search_result.asp?params=Installation:1;'
        else:
            log_url = self.start_urls[0]
        logger.info('Scraped catalog - %s', log_url)
        self.driver.get('%s&Page=%s' % (self.start_urls[0], 1))
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "PHA4"))
            )
        except:
            pass
        selenium_response_text = self.driver.page_source
        response = Selector(text=selenium_response_text)
        last_page = response.xpath('//select[@id="CurrentPage"]/option[last()]/@value').extract_first()
        if last_page:
            l_page = int(last_page) + 1
        else:
            l_page = 2

        for page in range(1, l_page):
            self.driver.get('%s&Page=%s' % (self.start_urls[0], page))
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "PHA4"))
                )
            except:
                pass
            selenium_response_text = self.driver.page_source
            response = Selector(text=selenium_response_text)
            item['category'] = ', '.join(response.xpath('//span[@class="menuSelText"]/text()').extract())
            for each in response.xpath('//div[@id="setka"]').xpath('//div[contains(@id, "sot")]'):
                try:
                    item['url'] = re.compile('\d+').findall(each.xpath(
                        'a[contains(@id, "XAnchorIMG")]/@href'
                    ).extract_first())[0]
                    yield item
                except (TypeError, IndexError):
                    pass
            logger.info('Check page number %s', '%s of %s' % (page, l_page-1))
        self.driver.close()
        self.display.stop()
