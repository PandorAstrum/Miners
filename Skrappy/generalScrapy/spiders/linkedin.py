# -*- coding: utf-8 -*-
import scrapy


class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'

    # build urls and domain
    allowed_domains = ['quotes.toscrape.com']
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # build what to catch
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()

            yield { 'text' : text,
                    'author': author,
                    'tags': tags}

        # next page
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)