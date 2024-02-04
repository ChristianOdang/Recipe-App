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
        return render_template('recipe/index.html',results = data)
    except:
        return render_template('error/404.html')
    
# route for homepage (index)
@bp.route('/home')
def home():
    try:
        data = querry_api()
        
        return render_template('recipe/index.html', results = data)
    except:
        return render_template('error/404.html')
    
# for test during dev remove before deployment
@bp.route('/test')
def test():
    
    data = querry_api()
    return render_template('recipe/test.html', results = data)

# route for page details
@bp.route('/details', methods=['POST'])
def detail():
    
    # get form data from form
    uri = request.form['item-details']
    
    try:
        # pass the param to the api
        data = querry_uri(uri)
        
        # return view and data
        return render_template('recipe/detail.html', results = data)
    except:
        return render_template('error/404.html')


# cart object for post
@bp.route('/cart', methods=['POST'])
def cart():
    data = request.get_json()
    
    return redirect(url_for('core.cart_display', data = data))

# call the display url header
@bp.route('/cart_display')
def cart_display():
    
    # get data from the cart uri
    data = request.args.get('data')
    
    #check if the data is not none
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
        return render_template('recipe/cart.html', results = cart_dict_v, results_count = cart_dict_k)
    except:
        return render_template('error/404.html')

        