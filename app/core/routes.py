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
