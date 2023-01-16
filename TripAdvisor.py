from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor


class Hotel(Item):
    nombre= Field()
    #precio= Field()
    descripcion = Field()
    amenities =Field ()

class TripAdvisor(CrawlSpider):
    name= "Hoteles"
    custom_settings = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }
    star_url =['https://www.tripadvisor.com.mx/Hotels-g150768-Mexico-Hotels.html']
    #Tiempo de espera para un requerimiento
    download_delay= 2

    #Definicion de reglas
    #Indicamos donde tiene que ir
    rules = (
        Rule(
            LinkExtractor(
                allow=r'/Hotel_Review-'
            ),  follow= True,callback="parse_hotel"
         ),
    )
    def parse_item(self,response):
        sel=Selector(response)

        item = ItemLoader(Hotel(),sel)

        item.add_xpath('nombre',  '//h1[@id="HEADING"]/text()' )
        #  item.add_xpath('precio','//div[@class="fzleB b")]/text()')
        item.add_xpath('descripcion',' //div[@class="ui_column  "]//div[contains(@data-ssrev-handlers, "Description")]//text()')
        item.add_xpath('amenities',
                       '//div[@class="ui_column  "]//div[@class="OsCbb K"]/div[contains(@data-test-target, "amenity_text")]//text()')

        yield item.load_item()




