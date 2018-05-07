# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Parameters for selenium"
"""
import csv
import re
from collections import deque
from datetime import datetime
from time import sleep
from urllib.parse import urlsplit

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from Utility import appDirs


ROOT_DIR = "C:\\Users\\Ana Ash\\Desktop\\Miner\\Project"
DUMP_DIR = "C:\\Users\\Ana Ash\\Desktop\\Miner\\Project\\Dump"

GOOGLE_SEARCH_QUERY = ["Legal marketing company in USA"]

LINKEDIN_LOGIN_PAGE = "https://www.linkedin.com/"

PAGE_COUNT = 2

CHROME_PATH = "C:\\Users\\Ana Ash\\Desktop\\Miner\\Project\\Sel\\Binary\\chromedriver.exe"
DRIVER = webdriver.Chrome(CHROME_PATH)


def get_curr_date_time(strft="%Y_%b_%d_%H.%M.%S"):
    return datetime.now().strftime(strft)

# get output file name
CLIENT_NAME = ""
EXTRA_NAME = ""
def get_outputFile(client_name=CLIENT_NAME, extra=EXTRA_NAME):
    if not extra == "":
        return f"{client_name}_{extra}_{get_curr_date_time()}.csv"
    else:
        return f"{client_name}_{get_curr_date_time()}.csv"


def sleep_time(time=0.5):
    return sleep(time)

def combine_dict(*args):
    result = {}
    for dic in args:
        for key in (result.keys() | dic.keys()):
            if key in dic:
                result.setdefault(key, []).extend(dic[key])
    return result

# dict to csv method
_default_dict1 = {'header': ['row1', 'row2']}
_default_dict2 = {'header2' : ['row1', 'row2']}
_default_csv_dict_list = [_default_dict1, _default_dict2]
_tuple_dict_zipped = zip(_default_dict1, _default_dict2)
_tuple_dict_with_header_name_zipped = zip(_default_dict1['header'], _default_dict2['header2'])
_curr_path = appDirs.get_current_directory()
def dict_to_csv( filename="test.csv",
                 _dict_list=_default_csv_dict_list,
                 _dict_tuple=_tuple_dict_zipped,
                 _dict_tuple_with_header=_tuple_dict_with_header_name_zipped,
                 _path=_curr_path):
    """
    Function for creating a csv file with the provided dictionary list
    :param filename:
    :param _dict_list: list of dictionary
    :param _dict_tuple: tuple of dictionary
    :param _dict_tuple_with_header: tuple of dictionary with named keys
    :return:
    """
    final_out_file = _path + "\\" + filename
    with open(final_out_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = list(_dict_tuple)[0]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in _dict_tuple_with_header:
            writer.writerow(dict(zip(fieldnames, row)))


def scroll_to_reveal(driver=DRIVER, element="document.body"):
    """

    :param driver:
    :param element:
    :return:
    """
    last_height = driver.execute_script(f"return {element}.scrollHeight")  # Get scroll height
    while True:
        driver.execute_script(f"window.scrollTo(0, {element}.scrollHeight);")  # Scroll down to bottom
        sleep_time(2.0)  # Wait to load page
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script(f"return {element}.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    sleep_time(2.0)

def process_next_page(driver=DRIVER, next_page_tag=None):
    if not next_page_tag == '':
        try:
            sleep_time()
            # return driver.find_element_by_xpath(f"{next_page_tag}")
            return driver.find_element_by_class_name(f"{next_page_tag}")

        except NoSuchElementException:  # element not found
            print("Next link not found")
            return None


def get_page(driver=DRIVER, base_url="https://www.google.com", username="admin", password="admin"):
    """

    :param driver:
    :param base_url:
    :param username:
    :param password:
    :return:
    """
    if 'linkedin.com' in base_url:
        driver.get(LINKEDIN_LOGIN_PAGE)
        sleep_time()
        # login with credentials
        username_field = driver.find_element_by_class_name('login-email')
        username_field.send_keys(username)
        password_field = driver.find_element_by_class_name('login-password')
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        sleep_time()

    driver.get(base_url)

def isolate_area_drivers(driver=DRIVER, classname=None, tagname=None, xpath=None, many=True):
    if many:
        if not classname == None:
            return driver.find_elements_by_class_name(classname)
        elif not tagname == None:
            return driver.find_elements_by_tag_name(tagname)
        elif not xpath == None:
            return driver.find_elements_by_xpath(xpath)
    else:
        if not classname == None:
            return driver.find_element_by_class_name(classname)
        elif not tagname == None:
            return driver.find_element_by_tag_name(tagname)
        elif not xpath == None:
            return driver.find_element_by_xpath(xpath)

def make_soup(driver=DRIVER, utf_on=False):
    """

    :param driver:
    :param utf_on:
    :return:
    """
    html_doc = driver.page_source
    if utf_on:
        return BeautifulSoup(html_doc, 'lxml').encode('utf-8')
    else:
        return BeautifulSoup(html_doc, 'lxml')

def get_data(soup=None, tag=None, identifier=None, identifier_str=None, all=False):
    """

    :param soup:
    :param tag:
    :param identifier:
    :param identifier_str:
    :param all:
    :return:
    """
    if not soup == None:
        try:
            if not all:
                return soup.find(tag, {identifier : identifier_str})
            else:
                return soup.find_all(tag, {identifier: identifier_str})
        except:
            return None


def extract(data=None, text=False, title=False, href=False):
    if not data == None:
        if not text == None:
            return data.text
    else:
        return None


# get emails from website
def get_from_website(list_of_website, exception_list):
    emails = []
    tels = []
    if type(list_of_website) != list:
        web_list = [list_of_website]
    else:
        web_list = list_of_website

    for each_website in web_list:
        # a queue of urls to be crawled
        new_urls = deque([each_website])
        # a set of urls that we have already crawled
        processed_urls = set()
        # a set of crawled emails
        _emails = set()
        _tels = set()
        # process urls one by one until we exhaust the queue
        while len(new_urls):
        # move next url from the queue to the set of processed urls
            url = new_urls.popleft()
            processed_urls.add(url)
            # extract base url to resolve relative links
            parts = urlsplit(url)
            base_url = "{0.scheme}://{0.netloc}".format(parts)
            path = url[:url.rfind('/') + 1] if '/' in parts.path else url

            # get url's content
            print("Processing %s" % url)
            try:
                for e in exception_list:
                    if not e in url:
                        response = requests.get(url)
            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                # ignore pages with errors
                continue

            # extract all email addresses and add them into the resulting set
            new_emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I)
            new_tels = re.findall(r"\+\d{2}\s?0?\d{10}", response.text, re.I)
            # except:
            #     new_emails = "not found"
            #     new_tels = "no tel"
            # finally:
            # new_tels = set(re.findall(r"\+\d{2}\s?0?\d{10}
            _emails.update(new_emails)

            _tels.update(new_tels)
            # tels.append(new_tels)

            # create a beutiful soup for the html document
            soup = BeautifulSoup(response.text, 'lxml')

            # find and process all the anchors in the document
            for anchor in soup.find_all("a"):
                # extract link url from the anchor
                link = anchor.attrs["href"] if "href" in anchor.attrs else ''
                # resolve relative links
                if link.startswith('/'):
                    link = base_url + link
                elif not link.startswith('http'):
                    link = path + link

                if 'contact' in link:
                    # add the new url to the queue if it was not enqueued nor processed yet
                    if not link in new_urls and not link in processed_urls:
                        new_urls.append(link)

        print(_emails)
        print(_tels)
        emails.append(_emails)

    return emails, tels

# def make_dict(list_of_list, list_of_headers):
#     i = 0
#     tmp_dict = {}
#     while i<len(list_of_list):
#         tmp_dict[list_of_headers[i]] = list_of_list[i]
#         i =+ 1


#         _default_dict1 = {'header': ['row1', 'row2']}
#         _default_dict2 = {'header2': ['row1', 'row2']}
#         _default_csv_dict_list = [_default_dict1, _default_dict2]
#         _tuple_dict_zipped = zip(_default_dict1, _default_dict2)
#         _tuple_dict_with_header_name_zipped = zip(_default_dict1['header'], _default_dict2['header2'])
#         _curr_path = appDirs.get_current_directory()
#
#         def dict_to_csv(filename="test.csv",
#                         _dict_list=_default_csv_dict_list,
#                         _dict_tuple=_tuple_dict_zipped,
#                         _dict_tuple_with_header=_tuple_dict_with_header_name_zipped,
#                         _path=_curr_path):


def quit(driver=DRIVER):
    driver.quit()
