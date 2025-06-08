#import libraries
import scrapy
from ..items import Listings





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
                rooms = card.xpath(".//dd[@data-sentry-component='RoomsDefinition']/span/text()").get()
                floor = card.xpath(".//dd[@data-sentry-component='FloorsDefinition']/span/text()").get()
                seller = card.xpath(".//div[@data-sentry-source-file='SellerInfo.tsx']/span/text()").get()


                base_url = "https://www.otodom.pl"
                full_url = base_url + follow_url


                #meta store for url  to pass to next callback 
                main_page ={
                    "url": follow_url,
                    "rooms":rooms,
                    "floor":floor,
                    "seller":seller,
                }

                if not follow_url:
                    self.logger.warning("No listing url was found in a card")
                    continue
                # Print follow url to console
                print(f"Found follow URL: {follow_url}")


                yield scrapy.Request(url = full_url,
                                    callback=self.listingsData,
                                     meta={"main_page":main_page}
                                     )

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

    async def listingsData(self, response):
        #instantiate item model 
        Listing_item = Listings()

        #load up meta store
        main_page = response.meta['main_page']

        #extract data     
        #first section
        #Listing_item ['Id'] = response.xpath("//p[@data-sentry-element='DetailsProperty']/text()").get()
        Listing_item ['Url'] = main_page.get("url") #from meta store 
        Listing_item['Rooms'] = main_page.get("rooms") 
        Listing_item['Floor_Number']= main_page.get("floor") 
        Listing_item['Type_of_Advertiser'] = main_page.get("seller") 
        Listing_item ['Title'] = response.xpath("//h1[@data-sentry-element='Title']/text()").get()
        Listing_item ['Monthly_Cost'] = response.xpath("//strong[@data-sentry-element='Price']/text()").get()
        Listing_item ['Location'] = response.xpath("//a[@data-sentry-source-file='MapLink.tsx']/text()").get()

    #Apartment section

        '''
        fields = [
            'Surface_Area', 'Rooms', 'Heating', 'Floor_Number', 'Condition',
            'Availabitiy_Date', 'Operational_Cost', 'Deposit', 'Type_of_Advertiser'
        ]

        containers = response.xpath('//div[@data-sentry-element="StyledListContainer"]/div[@data-sentry-element="ItemGridContainer"]')

        for field, container in zip(fields, containers):
            Listing_item[field] = container.xpath('./p[2]/text()').get()
            
        print(Listing_item)
        '''
        yield Listing_item 



        #Apartment Section
        '''
        Listing['Surface_Area'] = response.xpath("").get
        Listing['Rooms'] = response.xpath("").get
        Listing['Heating'] = response.xpath("").get
        Listing['Floor_Number'] = response.xpath("").get
        Listing['Condition'] = response.xpath("").get
        Listing['Availabitiy_Date'] = 
        Listing['Operational_Cost'] = 
        Listing['Deposit'] = 
        Listing['Type_of_Advertiser'] = 
        Listing['Amenities'] = 
        

        #Building Section
        Listing['Building_Construction_Year'] = 
        Listing['Lift'] = 
        Listing['Type_of_Building'] = 
        Listing['Windows'] = 
        Listing['Security'] = 
        Listing['Additional_Features'] = 

        #Description
        Listing['Description'] = 

        '''

