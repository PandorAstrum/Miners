# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "spider run"
"""
import sys,os.path
sys.path.append('.\\Skrappy\\generalSkrapy\\spiders\\')
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log, signals
from scrapy.xlib.pydispatch import dispatcher

from Skrappy.generalScrapy.spiders import linkedin

spider_count = 0
number_of_spiders = 2

def stop_reactor_after_all_spiders():
    global spider_count
    spider_count = spider_count + 1
    if spider_count == number_of_spiders:
        reactor.stop()


dispatcher.connect(stop_reactor_after_all_spiders, signal=signals.spider_closed)

def crawl_resident_advisor():

    global spider_count
    spider_count = 0

    crawler = Crawler(Settings())
    crawler.configure()
    crawler.crawl(linkedin())
    crawler.start()

    log.start()
    log.msg('Running in reactor...')
    reactor.run()  # the script will block here
    log.msg('Reactor stopped.')


import scrapy

# --run a crawler in a script stuff
from pydispatch import dispatcher
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from pydispatch import dispatcher
from scrapy.utils.project import get_project_settings
# --run a crawler in a script stuff

# --the spiders
from Skrappy.generalScrapy.spiders import linkedin


# --the spiders

def run_a_spider_on_script(spider, signal=signals.item_passed, slot=None):
    '''
    @brief  A function given a spider run it. If a signal an a slot is given connect it

    @param  spider
            The spider itself

    @param  signal
            scrapy signal ( defualt item passed  )

    @param  slot
            Function to launch after the signal is triggered
    '''
    # The spider
    spiderObj = spider()

    # The process to execute the spider
    process = CrawlerProcess(get_project_settings())

    # if the slot is not None...
    if (slot is not None):
        # Connect the signal with the slot
        # When the signal triggers execute the slot
        dispatcher.connect(slot, signal)

    # Set in the process the spider
    process.crawl(spider)
    process.start()

    # finished the crawler