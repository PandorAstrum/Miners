# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from Utility import parameters
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_path = "C:\\Users\\Ana Ash\\Desktop\\Miner\\Project\\Sel\\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

# linkedin Login
driver.get("https://www.linkedin.com")
parameters.sleep_time()

username_field = driver.find_element_by_xpath('//*[@id="login-email"]')
username_field.send_keys(parameters.LINKEDIN_USERNAME)
password_field = driver.find_element_by_id("login-password")
password_field.send_keys(parameters.LINKEDIN_PASSWORD)
login_btn = driver.find_element_by_xpath("//*[@type='submit']")
login_btn.click()
parameters.sleep_time()

# system one (search in sales navigator)

# system two grab from google search query
driver.get("https://www.google.com/")
parameters.sleep_time()
for search_query in parameters.GOOGLE_SEARCH_QUERY:

    search_q = driver.find_element_by_name("q")
    search_q.send_keys(search_query)
    search_q.send_keys(Keys.RETURN)
    parameters.sleep_time(0.2)

    # what to grab and build
    result_url = driver.find_elements_by_tag_name("cite")
    result_url = [url.text for url in result_url]
    parameters.sleep_time()

# iteration per search result

# system three
# company_urls = ['brandsdistribution.com']
# for company_url in company_urls:
#
#     driver.get('https://www.linkedin.com/sales?trk=d_flagship3_nav')
#     sleep(1.0)
#     get_search_box = driver.find_element_by_id('global-nav-typeahead-input')
#     get_search_box.send_keys(company_url)
#     get_search_box.send_keys(Keys.RETURN)
#
#     sleep(2.0)



    # jobTitle = driver.find_element_by_xpath('//*[@class="facet-list"]/li[@class="jobTitle"]')
    #
    # jobTitle.click()