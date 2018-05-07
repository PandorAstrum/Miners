# -*- coding: utf-8 -*-
from scrapy.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.selector import HtmlXPathSelector

# from Skrappy.generalScrapy.items import GeneralscrapyItem

# from Utility.parameters import LINKEDIN_USERNAME, LINKEDIN_PASSWORD

import scrapy


class LinkedinSpider(InitSpider):
    name = 'linkedin'
    login_url = 'https://www.linkedin.com/uas/login'
    allowed_domains = ['linkedin.com']
    start_urls = [
        'https://www.linkedin.com/feed/?trk='
    ]

    def init_request(self):
        # """This function is called before crawling starts."""
        return Request(url=self.login_url, callback=self.login)

    def login(self, response):
        # """Generate a login request."""
        return FormRequest.from_response(response,
                                         formdata={'session_key': 'eacinhossain12@gmail.com', 'session_password': 'mozammil01685'},
                                         callback=self.check_login_response)

    def check_login_response(self, response):
        # """Check the response returned by a login request to see if we aresuccessfully logged in."""
        if "Sign Out" in response.body:
            self.log("\n\n\nSuccessfully logged in. Let's start crawling!\n\n\n")
            # Now the crawling can begin..

            return self.initialized()  # ****THIS LINE FIXED THE LAST PROBLEM*****

        else:
            self.log("\n\n\nFailed, Bad times :(\n\n\n")
            # Something went wrong, we couldn't log in, so nothing happens.

    def parse(self, response):
        self.log("\n\n\n We got data! \n\n\n")
        # hxs = HtmlXPathSelector(response)
        # sites = hxs.select('//ol[@id=\'result-set\']/li')
        items = []
        # for site in sites:
        #     item = GeneralscrapyItem()
        #     item['title'] = site.select('h2/a/text()').extract()
        #     item['link'] = site.select('h2/a/@href').extract()
        #     items.append(item)
        return items

        # build what to catch
        # quotes = response.xpath('//*[@class="quote"]')
        # for quote in quotes:
        #     text = quote.xpath('.//*[@class="text"]/text()').extract_first()
        #     author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
        #     tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()

            # yield { 'text' : text,
            #         'author': author,
            #         'tags': tags}

        # next page
        # next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        # absolute_next_page_url = response.urljoin(next_page_url)
        # yield scrapy.Request(absolute_next_page_url)