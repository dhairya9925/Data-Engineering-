import scrapy
from scrapy_splash import SplashRequest


class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['walmart.com', "flipkart.com", "amazon.com", "imdb.com"]
    start_urls = ['https://www.imdb.com/chart/moviemeter']  # Change this to any search query you want


    def parse(self, response):
        # Extracting product details
        # products = response.css('div.pt0-xl')   
        movies = response.css('li.ipc-metadata-list-summary-item')   


        for movie in movies:
            title = movie.css('h3.ipc-title__text::text').get()  # Product title
            print(f"Title = {title}\n\n")
            metadata = movie.css('span.cli-title-metadata-item::text').getall()  # Product price
            if len(metadata) > 1:
                duration = metadata[1]
            rating = movie.css('span.ipc-rating-star--rating::text').get()  # Product link
            link = movie.css('a.ipc-title-link-wrapper::attr(href)').get()  # Product link
            
        # products = response.css('div.pt0-xl')   

        # for product in products:
        #     title = product.css('span[data-automation-id = "product-title"]::text').get()  # Product title
        #     price = product.css('span.f2::text').get()  # Product price
        #     link = product.css('a::attr(href)').get()  # Product link
        # yield {
        #     "name": title,
        #     "duration": duration,
        #     "rating": rating,
        #     "link": link,
        # }
            yield {
                "name": title,
                "duration": duration,
                "rating": rating,
                "link": link,
            }
        