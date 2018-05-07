# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
import csv

from bs4 import BeautifulSoup
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque, defaultdict
import re

# from csv file or inside this file flag
from Utility.generic_parameters import DUMP_DIR

from_file = True

if from_file:
    # get the csv file
    filename = DUMP_DIR + '\\' + 'email.csv'
    # build search criteria list
    columns = defaultdict(list)  # each value in each column is appended to a list

    with open(filename) as f:
        reader = csv.DictReader(f)  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():  # go over each column name and value
                columns[k].append(v)  # append the value into the appropriate list
                # based on column name k


    for each_item in columns["Website"]:

        # build url
        # final_url = "http://www." + each_item

        # a queue of urls to be crawled
        new_urls = deque([each_item])

        # a set of urls that we have already crawled
        processed_urls = set()

        # a set of crawled emails
        emails = set()
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
                if not "javascript" in url and not "facebook" in url and not "constantcontact" in url:
                    response = requests.get(url)
            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                # ignore pages with errors
                continue

            # extract all email addresses and add them into the resulting set
            new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
            emails.update(new_emails)

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

        print(emails)
