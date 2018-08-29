from flask import Flask, render_template, request, redirect
#from myapp.data.module import MyModule
from ..data.browser import MyBrowser
import urllib

app = Flask(__name__, template_folder ='views')


@app.route('/')
@app.route('/pokemons/')
def pokemon_list():
    new_browser = MyBrowser()
    return render_template('pokemons.html', pokemons = new_browser.print_pokemons())

@app.route('/pokemons/<string:pokemon_name>')
def pokemon_details(pokemon_name):
    new_browser = MyBrowser()
    #print(new_browser.get_profile_pokemon(pokemon_name).img)
    return render_template('pokemon_details.html', pokemons = new_browser.get_profile_pokemon(pokemon_name))

@app.route('/search')
def search_engine():
    return render_template('search.html')

@app.route('/search_result', methods =['POST'])
def check_submit():
    query = "" 
    if request.form.get("type_mode") == "0":
        query_dict = {'types' : request.form.get("type1") + "," + request.form.get("type2") }
    elif request.form.get("type_mode") == "1":
        query_dict = {'types-seulement' : request.form.get("type1") + "," + request.form.get("type2") }
    
    query = str(urllib.parse.urlencode(query_dict))
    return redirect('/search_result/' + query)

@app.route('/search_result/<string:query>')
def search_result(query):
    print(query)
    new_browser = MyBrowser()
    return render_template('search_result.html', pokemons = new_browser.get_pokemons_search(query))






