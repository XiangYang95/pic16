# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 15:20:45 2018

@author: Xiang Yang Ng
"""
import scrapy

class PokedexSpider(scrapy.Spider):
    name = "pokedex"

    def start_requests(self):
        url = 'https://pokemondb.net/pokedex/national'

        yield scrapy.Request(url=url, callback=self.parse1)

    def parse1(self, response):
# =============================================================================
#         pokedex = response.css("span.infocard-tall")
#         pokemon_number = [poke.css("small:not(.aside)::text").
#                           extract_first() for poke in pokedex]
#         pokemon_name = [poke.css("a.ent-name::text").
#                         extract_first() for poke in pokedex]
#         item = {}
#         item["number"] = pokemon_number[:10]
#         item["name"] = pokemon_name[:10]
#         scrapy.Request.meta["item"] = item
# =============================================================================
                   
# =============================================================================
#         for pokemon in pokedex:
#             yield{
#                 "number": pokemon.css("small:not(.aside)::text").extract_first(),
#                 "name": pokemon.css("a.ent-name::text").extract_first()
#                     }
#         item = MyItem()
#         item['pokemon'] = response.url
#     request = scrapy.Request("http://www.example.com/some_page.html",
#                              callback=self.parse_page2)
#     request.meta['item'] = item
# =============================================================================
        pokedex = response.css("span.infocard-tall")
        #next_page = response.css('span.infocard-tall a.pkg::attr(href)')
        for pokemon in pokedex:
            if pokemon is not None:
                each_pokemon = {}
                each_pokemon["number"] = pokemon.css("small:not(.aside)::text").extract_first()
                                         
                each_pokemon["name"] = pokemon.css("a.ent-name::text").extract_first()
                next_page = pokemon.css('a.pkg::attr(href)').extract_first()
                to_next_page = response.urljoin(next_page)
                request = scrapy.Request(to_next_page, callback=self.parse2)
                request.meta["pokemon"] = each_pokemon
                yield request
                
        
        # ORGANIZE REQUEST
        #yield request

            
    def parse2(self, response):
        entry = response.css("div#dex-flavor+h2+table.vitals-table \
                     tbody tr:first-of-type td::text").extract_first()

        each_pokemon = response.meta["pokemon"]
        each_pokemon["entry"] = entry    
        yield each_pokemon
                

        #response.css("span.infocard-tall a.pkg::attr(href)").extract_first()
         #response.css("span.infocard-tall a.ent-name::text")[:10].extract()
         #response.css("span.infocard-tall small:not(.aside)::text")[:10].extract()
         #response.css("div#dex-flavor+h2+table.vitals-table tbody tr:first-of-type td::text").extract_first()