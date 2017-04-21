import scrapy
from dianping_gallery.items import Review

class DianpingSpider(scrapy.Spider):
    name = "dianping-spider"
    start_urls = [
        'http://www.dianping.com/member/44509194/reviews',
    ]
    def parse(self, response):
        user_id = response.css('.pic a::attr("href")').extract_first().split('/')[-1]
        user_name = response.css('div.head-user h2.name::text').extract_first()
        for review in response.css('div.J_rptlist'):
            idx =  review.css('.J_flower::attr("data-id")').extract_first()
            shop = review.css('a.J_rpttitle::text').extract_first()
            address = review.css('div.addres p::text').extract_first()
            time = review.css('div.info span::text').extract_first()
            rate = review.css('div.comm-rst span::attr("class")').extract_first().split()[1]
            content = review.css('div.comm-entry::text').extract()    
            shop_url = review.css('a.J_rpttitle::attr("href")').extract_first()  
            album_url = shop_url + '/photos/album/' + user_id

            yield scrapy.Request(
                            album_url, 
                            callback=self.get_image_urls,
                            headers = {
                                'Cache-Control': 'no-cache',
                                'Connection': 'keep-alive',
                                'Content-Encoding': 'gzip',
                                'Content-Language': 'zh-CN',
                                'Content-Type': 'text/html;charset=UTF-8',
                                'Date': 'Sat, 15 Apr 2017 11:03:33 GMT',
                                'Keep-Alive': 'timeout=5',
                                'Pragma': 'no-cache',
                                'Server': 'DPweb',
                                # 'Transfer-Encoding': 'chunked',
                                'User-Agent': 'Chrome/22.0.1207.1',
                                'Vary': 'Accept-Encoding'                              
                                },
                            meta = {
                            'user_id': user_id,
                            'idx': idx, 
                            'shop': shop,
                            'user_name': user_name,
                            'address': address,
                            'time': time,
                            'rate': rate,
                            'content': content
                            }
            )

        next_page = response.css('a.page-next::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def get_image_urls(self, response):
        m = response.request.meta
        image_urls = []
        for img in response.css('li.J_pic-set img'):
            src = img.css('::attr("data-src")').extract_first()
            if src is None:
                src = img.css('::attr("src")').extract_first()
            image_urls.append(src)       
        print("Begin downloading: Review & Photos by user:", m['user_name'], "at shop:", m['shop'])
        yield Review(idx = m['idx'], shop = m['shop'], user_name = m['user_name'], address = m['address'], time = m['time'], rate = m['rate'], content = m['content'], image_urls  = image_urls)
