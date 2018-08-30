
from weboob.browser import PagesBrowser, URL
from .pages.pokemon import PokemonPage
from .pages.pokemon_profile import PokemonProfile
from flask import request




class MyBrowser(PagesBrowser):
    BASEURL = 'https://www.pokebip.com'

    """
    Pages definition
    """
    
    pokemon = URL(r'/pokedex/pokemon$', PokemonPage)
    pokemon_profile = URL(r'/pokedex/pokemon/(?P<pokemon_name>.*)', PokemonProfile)
    pokemon_search  = URL(r'/pokedex/pokemon\?(?P<query>)', PokemonPage)
    

    def print_pokemons(self):
        self.pokemon.go()

        #for pokemon in self.page.get_pokemons():
            #print(pokemon.id, pokemon.name, pokemon.pokedex_id, pokemon.type)  
        return self.page.get_pokemons()

    def get_profile_pokemon(self, name):
        self.pokemon_profile.go(pokemon_name=name)
        print("Requested details for " + name)
        return self.page.get_pokemon_infos()
   
    def get_pokemons_search(self, query):
            
            self.pokemon_search.go(query=query)
            print (self.pokemon_search.go(query=query).url)
            print("Request for the query : " + query)
            return self.page.get_pokemons()
