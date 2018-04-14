# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Parameters for selenium"
"""

from datetime import datetime
from time import sleep

def get_curr_date_time(strft="%Y_%b_%d_%H.%M.%S"):
    return datetime.now().strftime(strft)

def sleep_time(time=0.5):
    return sleep(time)

GOOGLE_SEARCH_QUERY = ["Legal marketing company in USA"]

LINKEDIN_USERNAME = "eacinhossain12@gmail.com"
LINKEDIN_PASSWORD = "mozammil01685"

CLIENT_NAME = "Name"

OUT_FILE = f"{CLIENT_NAME}_{get_curr_date_time()}.csv"