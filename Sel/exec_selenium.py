# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Utility.parameters import CHROME_PATH, linkedin_login, scroll_to_reveal, PAGE_COUNT, process_next_page, sleep_time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(CHROME_PATH)

linkedin_login(driver)

scroll_to_reveal(driver)

# get next page tag id
next_page_tag = '//button[@class="next"]'

_next = process_next_page(driver, next_page_tag)  # check and collect next page

if _next is not None:
    _dict_list = []
    _dict = {}
    _page_count = 1
    _jobTitle = []
    _company_link = []
    _company_name = []
    _location_of_position = []

    while _next is not None:
        if _page_count == PAGE_COUNT:
            break
        # get data

        # isolated_field_each = driver.find_elements_by_class_name('job-card-search--column')
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")

        # acquire data
        isolated_div = soup.find_all('div', {"class": 'job-card-search--column'})
        _temp = []
        for _each_div in isolated_div:
            _temp.append(_each_div.find('h3',{"class": 'job-card-search__title lt-line-clamp lt-line-clamp--multi-line ember-view'}).text.strip())
    #         _t = _each_div.find('a', {"class" : 'job-card-search__company-name-link'})
    #         _company_link.append(_t['href'])
    #         _company_name.append(_t.find('h4', {"class" : 'job-card-search__company-name'}).text.strip())
    #         _location_of_position.append(_each_div.find('h5', {"class": 'job-card-search__location'}).text.strip().replace('Job Location\\n', ''))
        _jobTitle.append(_temp)
        _page_count += 1
        driver.execute_script("arguments[0].click();", _next)
        sleep_time(2.0)
        # _next = process_next_page(driver, next_page_tag)
    #
    print(_jobTitle)
    # print(_company_link)
    # print(_location_of_position)
    # print(_company_name)

