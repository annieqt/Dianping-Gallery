# Dianping-Gallery
Crawling text & images from Dianping and generating pretty static pages!

## Features

#### 1. Crawling text & images from a specific user's Dianping account and storing them locally
The downloaded images will be stored under <span style="color:#E74C3C;border:solid 1px #e1e4e5;font-weight: bold;">../imgs/</span>, sorted by  <span style="color:#E74C3C;border:solid 1px #e1e4e5;font-weight: bold;">/user/shop/</span>  
You can also custom images path by change in<span style="color:#E74C3C;border:solid 1px #e1e4e5;font-weight: bold;">IMAGES_STORE</span> in <span style="color:#E74C3C;border:solid 1px #e1e4e5;font-weight: bold;">settings.py</span>

![][folders]

![][images]  

The text reviews are exported in Json format in <span class="hl">review.json</span>
![][review]
#### 2. Generating pretty static pages from crawled data!
To Be Done..

## How to run:
#### 1. Configurations
* Set <span style="color:#E74C3C;border:solid 1px #e1e4e5;font-weight: bold;">start\_urls</span> in <span style="color:#E74C3C;border:solid 1px #e1e4e5;font-weight: bold;">dianping\_spider.py</span>
to the url of the review page that you want to crawl
#### 2. Run

Under <span style="color:#E74C3C;border:solid 1px #e1e4e5;font-weight: bold;">../Dianping-Gallery/dianping\_gallery/dianping\_gallery/spiders </span> run:   
`>> scrapy runspider dianping_spider.py -o review.json`



[folders]: ./preview/folders.png
[images]: ./preview/images.png
[review]: ./preview/review.png

</style>

