                                        #THIS IS WITHOUT USING SELENIUM
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from shutil import which
from selenium.webdriver.chrome.options import Options


class BookstoscrapeSpider(scrapy.Spider):
    page_no=2
    name = 'booksToScrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        books=response.xpath("//ol/li/article/h3/a")
        for book in books:
            link=book.xpath(".//@href").get()

            yield response.follow(url=link,callback=self.parse_books)

        next_page=f'https://books.toscrape.com/catalogue/page-{self.page_no}.html'
        if self.page_no<=3:
            self.page_no+=1
            yield  response.follow(url=next_page,callback=self.parse)



    def parse_books(self,response):
        name=response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get()
        price=response.xpath("//div[@class='col-sm-6 product_main']/p[1]/text()").get()

        yield {
            'name':name,
            'price':price
        }