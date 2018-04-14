# -*- coding: utf-8 -*-
import scrapy


class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'

    # build urls and domain
    allowed_domains = ['google.com']
    start_urls = ['https://www.google.com/search?source=hp&ei=geHQWvm9F8T2vAS6roOoBA&q=legal+marketing+company&oq=legal+marketing+company&gs_l=psy-ab.3..0i22i30k1l2j0i22i10i30k1j0i22i30k1.647.12381.0.12668.26.20.0.0.0.0.386.3110.2-6j5.11.0....0...1c.1.64.psy-ab..15.11.3107.0..0j46j35i39k1j0i67k1j0i131k1j0i3k1j0i46k1.0.95r_aZtrsjg']

    def parse(self, response):
        # build what to catch
        company_name = response.xpath('//h3/a/text()').extract()
        company_urls = response.xpath('//h3/a/@href').extract()

        for company_url in company_urls:
            pass

        # return the catch
        yield {'Company Name' : company_name,
               'Company URL' : company_urls}
