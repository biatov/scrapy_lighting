import logging

BOT_NAME = 'lighting'

SPIDER_MODULES = ['lighting.spiders']
NEWSPIDER_MODULE = 'lighting.spiders'

USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'

ROBOTSTXT_OBEY = False

LOG_LEVEL = 'INFO'
logging.getLogger('scrapy').propagate = False

ITEM_PIPELINES = {
   'lighting.pipelines.LightingPipeline': 300,
}
