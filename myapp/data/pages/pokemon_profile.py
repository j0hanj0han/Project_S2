import re

from myapp.app.models.pokemon import Pokemon
#from app.models.pokemon import Pokemon

from weboob.browser.pages import HTMLPage
from weboob.capabilities.base import BaseObject, Field, StringField, IntField
from weboob.browser.elements import TableElement, ItemElement, method
from weboob.browser.filters.standard import CleanText, CleanDecimal, TableCell
from weboob.browser.filters.html import Attr


class PokemonProfile(HTMLPage):
    @method
    class get_pokemon_infos(ItemElement):
    
        klass = Pokemon
        obj_pv = CleanText('//div[contains(., "Aper")]/following-sibling::table//tr[2]/td[2]')
        obj_img = CleanText('//*[@id="content"]/div[4]/div[1]/div/img/@src')
        
              
