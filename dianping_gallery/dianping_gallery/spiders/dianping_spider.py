import scrapy
from dianping_gallery.items import Review

class DianpingSpider(scrapy.Spider):
    name = "dianping-spider"
    start_urls = [
        'http://www.dianping.com/member/917575728/reviews',
    ]

    def parse(self, response):
        for review in response.css('div.J_rptlist'):       
            review_url = review.css('div.comm-photo a::attr("href")').extract_first()
            yield scrapy.Request(next_page, self.parse_review)

        next_page = response.css('a.page-next::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, self.parse)

    def parse_review(self, response):
        yield {
                    'title': review.css('a.J_rpttitle::text').extract_first(),
                    'address': review.css('div.addres p::text').extract_first(),
                    'time': review.css('div.info span::text').extract_first(),
                    'rate': review.css('div.comm-rst span::attr("class")').extract_first().split()[1],
                    'content': review.css('div.comm-entry::text').extract(),
                }