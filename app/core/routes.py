from flask import Blueprint,  render_template, request, url_for, redirect
import json
import requests
import ast
from core import favourites
import requests
import os
from core.validation import check_if_empty

bp = Blueprint('core', __name__)

# test route for blueprint


@bp.route('/bp')
def index():
    return 'This is bp chekcks'

# routes for index page


@bp.route('/')
def hello():

    try:
        # call the query api method
        data = querry_api()

        # pass data to view
        return render_template('recipe/index.html', results=data)
    except:
        return render_template('error/404.html')

# route for homepage (index)


@bp.route('/home')
def home():
    try:
        data = querry_api()

        return render_template('recipe/index.html', results=data)
    except:
        return render_template('error/404.html')

# for test during dev remove before deployment


@bp.route('/test')
def test():

    data = querry_api()
    return render_template('recipe/test.html', results=data)

# route for page details


@bp.route('/details', methods=['POST'])
def detail():

    # get form data from form
    uri = request.form['item-details']

    try:
        # pass the param to the api
        data = querry_uri(uri)

        # return view and data
        return render_template('recipe/detail.html', results=data)
    except:
        return render_template('error/404.html')


# cart object for post
@bp.route('/cart', methods=['POST'])
def cart():
    data = request.get_json()

    return redirect(url_for('core.cart_display', data=data))

# call the display url header


@bp.route('/cart_display')
def cart_display():

    # get data from the cart uri
    data = request.args.get('data')

    # check if the data is not none
    if data:
        # convert to valid json uninf ast module
        data_to_json = ast.literal_eval(data)

        cart_dict_v = []
        cart_dict_k = []

        for k, v, in data_to_json.items():
            cart_dict_k.append(v)
            cart_dict_v.append(query_uri(k))

    else:
        cart_dict_v = []
        cart_dict_k = []

    try:
        return render_template('recipe/cart.html', results=cart_dict_v, results_count=cart_dict_k)
    except:
        return render_template('error/404.html')

# Url for search results


@bp.route('/search', methods=['POST'])
def process_data():
    # get post data using request
    data = request.get_json()

    # redirect to search page
    return redirect(url_for('core.search_recipe',
                            search=data['search'],
                            select=data['selected_option']))

# search recipe


@bp.route('/search_recipe')
def search_recipe():
    # get values from form fields
    search = request.args.get('search')
    select = request.args.get('select')

    # call API with the search field
    results = querry_api(search, select)

    # format data for view for diet and ingredients
    search_data = ['', '', 'Diets', 'Ingredients']

    # check the users selected options
    if select == '0' or select == '1':

        # return the user input to the view
        search = search
    else:
        # return the value of the view
        search = search_data[int(select)]

    # render the templates with the view data
    return render_template('recipe/result.html',
                           results=results, search=search)
    
# route for about page
@bp.route('/about')
def about():
    
    return render_template('profile/about.html')

# rerun contact page
@bp.route('/contact')
def contact():
    
    return render_template('profile/contact.html')

# favourite route
@bp.route('/browse', methods=['POST'])
def browse():
    # get post data using request
    data = request.get_json()
    
    # check if result already in db
    if not favourites.get_item(data):
        data_resp = favourites.add_favourite(data)
    else:
        pass
    return render_template('')

@bp.route('/favourite')
def favourite():
    try:
        results = favourites.get_all()
        api_data = []
        for result in results:
            api_data.append(query_uri(result.favourites))
            
        # print(api_data)
        return render_template('favourite/home.html', results=api_data)
    except:
        return render_template('error/404.html')

@bp.route('/remove_favourite', methods=['POST'])
def remove_fav():
    try:
        # get from uri from
        uri = request.form['favourite-id']
        
        # remove item from favourite
        favourites.remove_uri(uri)
        
        # redirect method
        return favourite()
    except:
        return render_template('error/404.html')
    
def querry_api(querry_string=None, select_category=None):
    # get API pram from env
    app_key = os.getenv('API_KEY')
    app_id = os.getenv('API_ID')
    
    # process url for api query
    param = {
        'app_id' : app_id,
        'api_key': app_key
    } 
    
    # format url for api query
    if select_category == '0':
        base_url = 'https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}&q={}'.format(app_id,app_key,querry_string)  
    elif select_category == '1':
        base_url = 'https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}&cuisineType={}'.format(app_id,app_key,querry_string)
    elif select_category == '2':
        base_url = 'https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}&diet={}'.format(app_id,app_key,querry_string)
    elif select_category == '3':
        base_url = 'https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}&ingr={}'.format(app_id,app_key,querry_string)
    else:
        base_url = 'https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}&diet=balanced'.format(app_id,app_key)    
    
    try:
        # querry api
        resp = requests.get(base_url, params=param)
        
        # convert to json
        data = json.loads(resp.text)
        
        # return api data
        return data
    except requests.exceptions.ConnectionError as e:
        print('', e)
        data = {'connection':'Not connected! Please  check your internet connectivity'}
        return data
    
# make api call using uri
def query_uri(url):
    
    # get API pram from env
    app_key = os.getenv('API_KEY')
    app_id = os.getenv('API_ID')
    
    # processe api param
    param = {
        'app_id' : app_id,
        'api_key' : app_key,
        'uri' : url
    }
    
    # format base uri
    base_url = "https://api.edamam.com/api/recipes/v2/by-uri?type=public&app_id={}&app_key={}&uri={}".format(app_id,app_key,url)
    
    try:
        # make API call
        resp = requests.get(base_url, params=param)
        
        # convert to json
        data = json.loads(resp.text)
        
        # return data
        return data
    except requests.exceptions.ConnectionError as e:
        print('', e)
        data = {'connection': 'Not connection! Please check your internet connectivity'}
        return data
    