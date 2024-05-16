import scrapy
import json

class OlxPlacas(scrapy.Spider):
    name = 'olx'

    custom_settings = {
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'AUTOTHROTTLE_ENABLED' : True,
    }

    def start_requests(self):
        ''
        yield scrapy.Request('https://www.olx.com.br/informatica/placas-de-video')

    def parse(self, response, **kwargs):
        html = json.loads(response.xpath('//script[@id="__NEXT_DATA__"]/text()').get())
        placas = html.get('props').get('pageProps').get('ads')
        for placa in placas:
            yield{
                'title' : placa.get('title'),
                'price' : placa.get('price'),
                'locations' : placa.get('location')
            }