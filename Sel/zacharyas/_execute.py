# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from Sel.zacharyas.parameters import CLIENTS_NAME, BASE_URL
from Utility.parameters import get_page, make_soup, quit, get_data, get_from_website, process_next_page
from Utility.parameters import get_outputFile, dict_to_csv, scroll_to_reveal
from Utility.parameters import sleep_time, DUMP_DIR, CHROME_PATH, DRIVER

from Utility.generic_parameters import LINKEDIN_USERNAME, LINKEDIN_PASSWORD, WEBSITE_EXCEPTION_LIST

get_page(base_url=BASE_URL, username=LINKEDIN_USERNAME, password=LINKEDIN_PASSWORD)

# data to store
company_name = []
company_website_linkedin = []
job_name = []
job_location = []
job_position = []
company_size = []

# get basic data

# search for every company


page_count = 1
to_page = 8

while page_count < to_page:
    sleep_time(2.0)
    scroll_to_reveal()
    sleep_time(2.0)
    _next_page = DRIVER.find_element_by_class_name('next')
    if _next_page != None:

        soup = make_soup()

        # job name
        _job_name_div = soup.find_all('div', {'class' : 'job-card-search__content-wrapper'})
        for i in _job_name_div:
            try:
                _job_name = i.find('h3', {'class' : 'job-card-search__title'}).text
                _company_name = i.find('h4', {'class' : 'job-card-search__company-name'}).text
                _company_linkedin = i.find('a', {'class' : 'job-card-search__company-name-link'})['href']
                _job_location = i.find('h5', {'class' : 'job-card-search__location'}).text
            except:
                _job_name = "Not Found"
                _company_name = "Not Found"
                _company_linkedin = "No LInk"
                _job_location = "No location"
            finally:
                job_name.append(_job_name)
                company_name.append(_company_name)
                company_website_linkedin.append(_company_linkedin)
                job_location.append(_job_location)

        sleep_time(2.0)
        _next_page.click()

    page_count += 1

job_name_dict = {}
company_name_dict = {}
company_website_linkedin_dict = {}
job_location_dict = {}
job_name_dict['JOB TITLE'] = job_name
company_name_dict['Company Name'] = company_name
company_website_linkedin_dict['LINKEDIN URL'] = company_website_linkedin
job_location_dict['JOB LOCATION'] = job_location

_filename = get_outputFile(client_name=CLIENTS_NAME, extra='admin_assistant_tampa')
_dict_list = [job_name_dict, company_name_dict, company_website_linkedin_dict, job_location_dict]
_tuple_dict_zip = zip(job_name_dict, company_name_dict, company_website_linkedin_dict, job_location_dict)

_tuple_dict_with_header_name_zipped = zip(job_name_dict['JOB TITLE'],
                                          company_name_dict['Company Name'],
                                          company_website_linkedin_dict["LINKEDIN URL"],
                                          job_location_dict["JOB LOCATION"])

dict_to_csv(filename=_filename,
                 _dict_list=_dict_list,
                 _dict_tuple=_tuple_dict_zip,
                 _dict_tuple_with_header=_tuple_dict_with_header_name_zipped,
                 _path=DUMP_DIR)

quit()
