# Dianping-Gallery
Crawling text & images from Dianping and generating pretty static pages!

## Features

#### 1. Crawling text & images from a specific user's Dianping account and storing them locally
The downloaded images will be stored under `../imgs/`, sorted by `/user/shop/`   
You can also custom images path by change in `IMAGES_STORE` in `settings.py`

![][folders]
![][images]  

The text reviews are exported in Json format in `review.json`
![][review]
#### 2. Generating pretty static pages from crawled data!
To Be Done..

## How to run:
#### 1. Configurations
* Set `start\_urls` in `dianping\_spider.py` to the url of the review page that you want to crawl
#### 2. Run

Under `../Dianping-Gallery/dianping\_gallery/dianping\_gallery/spiders`, run:   
`>> scrapy runspider dianping_spider.py -o review.json`



[folders]: ./preview/folders.png
[images]: ./preview/images.png
[review]: ./preview/review.PNG
