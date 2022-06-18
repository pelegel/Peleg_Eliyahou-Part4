from flask import Blueprint, render_template

# menu blueprint definition
menu = Blueprint('menu', __name__,
                 static_folder='static',
                 static_url_path='/menu',
                 template_folder='templates')
