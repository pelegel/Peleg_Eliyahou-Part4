from flask import Blueprint, render_template

#assignment3_1 blueprint definition
home = Blueprint('home', __name__,
                 static_folder='static',
                 static_url_path='/home',
                 template_folder='templates')


#routes
@home.route('/home')
@home.route('/')
def home_page():
    return render_template('Home.html')
