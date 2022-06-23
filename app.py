from flask import Flask, redirect, render_template
from flask import url_for
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector
import time
import requests

###### App setup
from utilities.db_manager import interact_db

app = Flask(__name__)
app.config.from_pyfile('settings.py')


app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)


###### Components
## menu
from components.menu.menu import menu
app.register_blueprint(menu)


# root of our website


##home
from pages.home.home import home
app.register_blueprint(home)

##contact
from pages.contact.contact import contact
app.register_blueprint(contact)

##assignment3_1
from pages.assignment3_1.assignment3_1 import assignment3_1
app.register_blueprint(assignment3_1)

##assignment3_2
from pages.assignment3_2.assignment3_2 import assignment3_2
app.register_blueprint(assignment3_2)

##assignment4
from pages.assignment4.assignment4 import assignment4
app.register_blueprint(assignment4)





#dictionary of the session
@app.route('/session')
def session_func():
    return jsonify(dict(session))






if __name__ == '__main__':
    app.run(debug=True)


