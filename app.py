from flask import Flask, redirect, render_template
from flask import url_for
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector
import time
import requests

###### App setup
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


@app.route('/assignment4/outer_source')
def outer_source_func():
    return render_template('assignment4_outer_source.html')






def get_specific_user(id):
    users = []
    for i in range(id):
        res = requests.get(f'https://reqres.in/api/users/{id}')
        print(res)
        users.append(res.json())
    return users



@app.route('/fetch_fe')
def fetch_fe_func():
    if 'type' in request.args:
        user_id = int(request.args['user_num_fetch_fe'])

        # SYNC
        if request.args['type'] == 'sync':
            users = get_specific_user(user_id)
            session['user_id_fe'] = user_id

    return render_template('assignment4.html')






def get_users_sync():
    users = []
    res = requests.get(f'https://reqres.in/api/users')
    users_data = res.json()
    user = users_data['data']
    users.append(user)
    return users



def save_users_to_session(users, user_id):
    user_to_save = []
    users_data = users[0]
    for user in users_data:
        if user['id'] == user_id:
            users_dict = {
                'first_name': user['first_name'],
                'email': user['email'],
                'avatar': user['avatar']
            }
            user_to_save.append(users_dict)
            print(user_to_save)

    session['user'] = user_to_save





@app.route('/fetch_be')
def fetch_be_func():
    session.clear()

    if 'type' in request.args:
        user_id = int(request.args['user_num_fetch_be'])
        users = []

        # SYNC
        if request.args['type'] == 'sync':
            users = get_users_sync()

        save_users_to_session(users, user_id)

    else:
        session.clear()

    print(session)
    return render_template('assignment4.html')




if __name__ == '__main__':
    app.run(debug=True)


