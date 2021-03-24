import scrapy


class ComputeritemsSpider(scrapy.Spider):
    name = 'computerItems'
    page_number=2
    allowed_domains = ['www.sastodeal.com']
    start_urls = ['https://www.sastodeal.com/electronic/computer-laptop-peripherals.html']

    def parse(self, response):
        items=response.xpath("//ol[@class='products list items product-items']/li/div")
        for item in items:
            link=item.xpath(".//a/@href").get()
            name=item.xpath(".//div/strong/a/text()").get()
            original_price=item.xpath(".//div/div/span[1]/span/span/span/text()").get()
            discounted_price=item.xpath(".//div/div/span[2]/span/span/span/text()").get()
            yield {
                'item_link':link,
                'item_name':name,
                'discounted_price':discounted_price,
                'original_price':original_price
            }

        next_page = 'https://www.sastodeal.com/electronic/computer-laptop-peripherals.html?p='+ str(ComputeritemsSpider.page_number)
        print(next_page)
        if ComputeritemsSpider.page_number < 6:
            ComputeritemsSpider.page_number += 1
            print(ComputeritemsSpider.page_number)
            yield response.follow(next_page,self.parse)  #forbidden by robots.txt otherwise would work
