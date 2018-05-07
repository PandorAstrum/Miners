# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Utility.parameters import CHROME_PATH, OUT_FILE
from Utility.parameters import dict_to_csv, sleep_time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(CHROME_PATH)

# los angeles
los_angeles_url = "https://classpass.com/explore/5TAvjLvJsr7-los-angeles-orange-county-fitness-classes"
los_angeles_zip = range(90001, 91610)

# miami
miami_url = "https://classpass.com/explore/3qDTLb6b2UX-miami-south-florida-fitness-classes"
miami_zip = [33101,33109,33111,33114,33125,33126,33127,33128,33129,33130,33131,33132,33133,33134,33135,33136,33137,33138,33139,33140,33142,33144,33145,33146,33147,33149,33150,33151,33159,33222,33233,33234,33238,33242,33245,33255]

# honolulu
honolulu_url = "https://classpass.com/explore/4xsuWJ6p135-honolulu-fitness-classes"
honolulu_zip = [96795,96801,96802,96803,96804,96805,96806,96807,96808,96809,96810,96811,96812,96813,96814,96815,96816,96817,96818,96819,96820,96821,96822,96823,96824,96825,96826,96828,96830,96836,96837,96838,96839,96840,96841,96843,96844,96846,96847,96848,96849,96850,96853,96858,96859,96898]

# inland empire
inland_empire_url = "https://classpass.com/explore/3sHjVsdrxco-inland-empire-fitness-classes"
inland_empire_zip = [92501,92503,92504,92505,92506,92507,92508,92509,92879,92880,92881,92882,92883,92860,91708,91710,91758,91761,91762,91764,91763,91711,92590,92591,92592,92562,92530,92532,92401,92403,92404,92405,92407,92408,92410,92411,92373,92374,92313,92324,92343,92324,91701,91730,91737,91739,91765,91766,91767,91768,91784,91785,91786,92392,92394,92395,92344,92345,92310,92311,92312,92262,92264,92210,92211,92260,92234,92270,92223,92220,92331,92334,92335,92336,92337,92376,92377]

# missoula
missoula_url = "https://classpass.com/explore/5wjMDN8gK91-missoula-fitness-classes"
missoula_zip = [59801, 59802, 59803, 59806, 59807, 59808, 59812]

# get the base url
driver.get(miami_url)

company_name = []
company_location = []
company_desc = []

# for every area code list
for x in miami_zip:
    sleep_time(2.0)
    # get the area code on search box and enter
    zip_search_input = driver.find_element_by_id('zip_field')
    zip_search_input.send_keys(str(x))
    zip_search_input.send_keys(Keys.RETURN)

    sleep_time(2.0)

    # get the data
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'lxml')

    _company_name_list = soup.find_all('h5', {"class" : 'mb--'})

    for _each_company_name in _company_name_list:
        company_name.append(_each_company_name.text)

    _company_location = soup.find_all('p', {"class" : 'studio-list-item__location mb-'})

    for _each_company_location in _company_location:
        company_location.append(_each_company_location.text)

    _company_desc = soup.find_all('p', {"class" : 'text--light'})

    for _each_company_desc in _company_desc:
        company_desc.append(_each_company_desc.text)

    sleep_time(2.0)

    zip_search_input.clear()

    # merge with new or existing dict

# final dict
company_name_dict = {}
company_name_dict["company_name"] = company_name

company_location_dict = {}
company_location_dict["company_location"] = company_location

company_desc_dict = {}
company_desc_dict["company_description"] = company_desc

toCSV = [company_name_dict, company_location_dict, company_desc_dict]

keys = toCSV[0].keys()

with open(OUT_FILE, 'w', newline='') as csvfile:
    fieldnames = list(zip(company_name_dict, company_location_dict, company_desc_dict))[0]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in zip(company_name_dict['company_name'], company_location_dict['company_location'], company_desc_dict['company_description']):
        writer.writerow(dict(zip(fieldnames, row)))
# with open(OUT_FILE, 'wb') as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(toCSV)



    # get data in list and prepare fro writing csv

