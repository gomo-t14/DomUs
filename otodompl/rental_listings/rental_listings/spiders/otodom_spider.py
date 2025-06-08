#import libraries
import scrapy





#define spider
class OtodomSpider(scrapy.Spider):
    name = 'otodom'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    

    #urls
    start_urls = [
        "https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/cala-polska?limit=36&by=DEFAULT&direction=DESC&viewType=listing" #url for rental apartments in poland

    ]


    def parse(self, response):
        try:
            cards = response.xpath("//article[@data-cy='listing-item']")
            if not cards:
                self.logger.warning("No listing cards found on this page.")
        except Exception as e:
            self.logger.error(f"Error while parsing listing cards: {e}")
            cards = []

        for card in cards:
            try:
                follow_url = card.xpath(".//a[@data-cy='listing-item-link']/@href").get()
                if not follow_url:
                    self.logger.warning("No listing url was found in a card")
                    continue
                follow_url = response.urljoin(follow_url)

                # Print follow url to console
                print(f"Found follow URL: {follow_url}")
                #yield scrapy.Request(follow_url, callback=self.parse_job)

            except Exception as e:
                self.logger.error(f"Error while parsing listing url: {e}")
                continue



        #pagination 
        page_num = 2
        url = f"https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/cala-polska?limit=36&by=DEFAULT&direction=DESC&viewType=listing&page={page_num}"
       
        #quick fix but return later 
        if page_num < 3:
            yield scrapy.Request(url = url , callback=self.parse)
            page_num =+ 1
            print('New Page')

