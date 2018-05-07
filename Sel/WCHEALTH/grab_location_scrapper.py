# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
import csv
from collections import defaultdict
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from Utility.parameters import CHROME_PATH, DUMP_DIR
from Utility.parameters import sleep_time

# get the csv file
filename = DUMP_DIR + '\\' + 'WCHEALTH_missoula_2018_Apr_18_03.32.44.csv'

# build search criteria list
columns = defaultdict(list) # each value in each column is appended to a list

with open(filename) as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k
data = ['site:classpass.com/studios/' + col1+' '+col2 for col1,col2 in zip(columns['Company Name'],columns['Company Location'])]

# open up google
driver = webdriver.Chrome(CHROME_PATH)



temp_url_list = []
for d in data:

    # get google
    driver.get('https://www.google.com/')
    driver.maximize_window()
    sleep_time()
    # find search box
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(d)
    search_box.send_keys(Keys.RETURN)
    # get first selection url and click
    temp_doc = driver.page_source
    temp_soup = BeautifulSoup(temp_doc, 'lxml')
    ss = temp_soup.find('h3', {"class" : 'r'})
    dd = ss.find('a')['href']

    sleep_time()

# for each list item
print(temp_url_list)
address_list = []
for t in temp_url_list:
    driver.get(t)
    sleep_time(1.0)
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'lxml')
    address_div = soup.find('div', {"class": 'venue__header__detail__details'})
    address_line = address_div.find('address').text
    address_list.append(address_line)
    sleep_time(1.0)



