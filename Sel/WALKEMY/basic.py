# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException

from Utility.parameters import get_page, make_soup, quit, get_data, get_from_website
from Utility.parameters import get_outputFile, dict_to_csv, scroll_to_reveal
from Utility.parameters import sleep_time, DUMP_DIR
from Utility.generic_parameters import CLIENTS_NAME, BASE_URL
from Utility.generic_parameters import LINKEDIN_USERNAME, LINKEDIN_PASSWORD, WEBSITE_EXCEPTION_LIST

get_page(base_url=BASE_URL, username=LINKEDIN_USERNAME, password=LINKEDIN_PASSWORD)

# data to store
company_name = []
company_website = []
company_location = []
company_phone_number = []
generic_email = []

scroll_to_reveal()

soup = make_soup()

all = get_data(soup=soup, tag='div', identifier='class', identifier_str='member-directory-wrap', all=True)

for a in all:
    try:
        c_name = a.find('a').text
        c_link = a.find('a')['href']
        c_location = a.find('small').text
    except:
        c_name = a.find('strong').text
        c_link = "No link"
        c_location = "No Location"
    finally:
        company_name.append(c_name)
        company_website.append(c_link)
        company_location.append(c_location)

quit()
# generic_email, company_phone_number = get_from_website(company_website, WEBSITE_EXCEPTION_LIST)


# TODO : output to csv
company_name_dict = {}
company_website_dict = {}
# company_phone_number_dict = {}
company_location_dict = {}
# generic_email_dict = {}
company_name_dict["Company Name"] = company_name
company_website_dict["Website"] = company_website
# company_phone_number_dict["Telephone"] = company_phone_number
company_location_dict["Location"] = company_location
# generic_email_dict["Email"] = generic_email
dict_list = [company_name_dict, company_website_dict, company_location_dict]
tuple_dict_zipped = zip(company_name_dict, company_website_dict, company_location_dict)
tuple_dict_with_header_name_zipped = zip(company_name_dict['Company Name'],
                                         company_website_dict['Website'],
                                         company_location_dict["Location"])

output_file = get_outputFile(client_name=CLIENTS_NAME)
dict_to_csv(filename=output_file,
            _dict_list=dict_list,
            _dict_tuple_with_header=tuple_dict_with_header_name_zipped,
            _dict_tuple=tuple_dict_zipped,
            _path=DUMP_DIR)
