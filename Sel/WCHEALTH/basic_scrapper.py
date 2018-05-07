# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
import csv

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Utility.parameters import CHROME_PATH, DUMP_DIR
from Utility.parameters import dict_to_csv, sleep_time, get_outputFile, scroll_to_reveal
from bs4 import BeautifulSoup

driver = webdriver.Chrome(CHROME_PATH)

# base parameter
CLIENT_NAME = "WCHEALTH"

base_url = "https://classpass.com/studios"

_company_name = []
_company_url = []
_company_location = []
_company_location_map_url = []
_company_map = []
_company_website = []
_company_telephone = []



New_York_Metro_done = 1
Los_Angeles_Orange_County_Metro_done = 2
San_Francisco_Bay_Area_done = 3
Chicago_Metro_done = 4
Miami_South_Florida_Metro_done = 5
Boston_Metro_done = 6
Washington_D_C_Metro_done = 7
Seattle_Metro_done = 8
Atlanta_Metro_done = 9
Austin_Metro_done = 10
Charlotte_Metro_done = 11
Columbus_Metro_done = 12
Dallas_Fort_Worth_Metro_done = 13
Denver_Boulder_Metro_done = 14
Houston_Metro_done = 15
Minneapolis_St_Paul_Metro_done = 16
Philadelphia_Metro_done = 17
Phoenix_Scottsdale_Metro_done = 18
Portland_Metro_done = 19
San_Diego_Metro_done = 20
Las_Vegas_Metro_done = 21
Raleigh_Metro_done = 22
Baltimore_Metro_done = 23
Tampa_Metro_done = 24
St_Louis_Metro_done = 25
Orlando_Metro_done = 26
Nashville_Metro_done = 27
Sacramento_Metro_done = 28
Kansas_City_Metro_done = 29
Cincinnati_Metro_done = 30
Pittsburgh_Metro_done = 32
Milwaukee_Metro_done = 34
New_Orleans_Metro_done = 43
San_Antonio_Metro_done = 44
Indianapolis_Metro_done = 45
Salt_Lake_City_Metro_done = 46
Honolulu_Metro_done = 47
Inland_Empire_Metro_done = 49
Missoula_Metro_done = 50

selection_value_list = [Milwaukee_Metro, ]
driver.get(base_url)
sleep_time(1.0)
# list button click
driver.find_element_by_xpath('//*[@id="main"]/search/div/div[1]/aside/div/div[2]/ul/li[2]/a').click()
sleep_time(1.0)
selection_dropdown = Select(driver.find_element_by_xpath('//*[@id="main"]/search/div/div[1]/aside/div/div[1]/select'))
# get company url in class pass
for i in selection_value_list:
    sleep_time(3.0)
    # selection input dropdown
    selection_dropdown.select_by_value(str(i))
    sleep_time(3.0)
    # scroll div
    scroll_div = driver.find_element_by_xpath('//*[@id="main"]/search/div/div[2]/div')
    scroll_div.click()
    sleep_time(3.0)
    last_height = driver.execute_script('return arguments[0].scrollHeight; ', scroll_div)
    while True:
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight; ", scroll_div)
        sleep_time(4.0)  # Wait to load page
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return arguments[0].scrollHeight; ", scroll_div)
        if new_height == last_height:
            break
        last_height = new_height
    sleep_time(4.0)
    # gather data
    html_doc = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html_doc, 'lxml')

    _company = soup.find_all('li', {"class": 'js-infinite-scroll-item'})

    for every_list_item in _company:
        name_url = every_list_item.find('a', attrs={"target":'_self'})['href']
        if name_url not in _company_url:
            _company_url.append(name_url)

    sleep_time(4.0)

    print(_company_url)
    print(len(_company_url))

iteration = 0
# get name, location and map for every company
for url in _company_url:
    sleep_time()
    iteration += 1
    print(iteration)
    driver.get(url)

    #grab all required data
    sleep_time(1.0)
    html_doc2 = driver.page_source.encode('utf-8')
    soup2 = BeautifulSoup(html_doc2, 'lxml')
    try:
        company_name = soup2.find('h1', {"class":'beta'}).text
    except:
        company_name = "No name"
    finally:
        _company_name.append(company_name)

    try:
        company_location_head = soup2.find('div', {"class" : 'venue__header__detail__details'})
        company_location = company_location_head.find('address').text
    except:
        company_location = "No location found"
    finally:
        _company_location.append(company_location)

    try:
        company_map = soup2.find('a', {"class": 'venue__header__map'})['href']
    except:
        company_map = "No map data"
    finally:
        _company_map.append(company_map)

    try:
        company_website = soup2.find('a', {"class" : 'venue__about__website'}).text
    except:
        company_website = "No website"
    finally:
        _company_website.append(company_website)

    try:
        company_telephone = soup2.find('a', {"class" : 'venue__about__phone'}).text
    except:
        company_telephone = "No Telephone"
    finally:
        _company_telephone.append(company_telephone)

# make the csv output
_company_name_dict = {}
_company_name_dict["Company Name"] = _company_name
_company_location_dict = {}
_company_location_dict["Company Location"] = _company_location
_company_map_dict = {}
_company_map_dict["Company Map"] = _company_map
_company_telephone_dict = {}
_company_telephone_dict["Company Telephone"] = _company_telephone
_company_website_dict = {}
_company_website_dict["Website"] = _company_website

_filename = get_outputFile(client_name=CLIENT_NAME, extra="Milwaukee_Metro")
_dict_list = [_company_name_dict, _company_location_dict, _company_website_dict, _company_telephone_dict, _company_map_dict]
_tuple_dict_zip = zip(_company_name_dict, _company_location_dict, _company_website_dict, _company_telephone_dict, _company_map_dict)

_tuple_dict_with_header_name_zipped = zip(_company_name_dict['Company Name'],
                                          _company_location_dict['Company Location'],
                                          _company_website_dict["Website"],
                                          _company_telephone_dict["Company Telephone"],
                                          _company_map_dict['Company Map'])

dict_to_csv(filename=_filename,
                 _dict_list=_dict_list,
                 _dict_tuple=_tuple_dict_zip,
                 _dict_tuple_with_header=_tuple_dict_with_header_name_zipped,
                 _path=DUMP_DIR)

# exit
sleep_time()
driver.quit()
