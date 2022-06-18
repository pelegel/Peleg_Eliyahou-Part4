from flask import Flask, redirect, render_template
from flask import url_for
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')


app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)


userss = {'user1': {'name': 'Yossi', 'email': 'Yossi@gmail.com', 'password': 'Yossi12345'},
         'user2':  {'name': 'Dana', 'email': 'Dana@gmail.com', 'password': 'Dana12345'},
         'user3': {'name': 'Ron', 'email': 'Ron@gmail.com', 'password': 'Ron12345'},
         'user4': {'name': 'Noa', 'email': 'Noa@gmail.com', 'password': 'Noa12345'},
         'user5': {'name': 'Shir', 'email': 'Shir@gmail.com', 'password': 'Shir12345'}}

#list of user's details dictionaries
users_details = list(userss.values())

###### Components
## menu
from components.menu.menu import menu
app.register_blueprint(menu)


# root of our website
@app.route('/')
def index_func():
    return render_template('Home.HTML')






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



@app.route('/assignment3_2',  methods=['GET', 'POST'])
def assignment3_2_page():
    #for search
    if request.method == 'GET':
        if 'email' in request.args:
            email = request.args['email']

            if email == '':
                return render_template('assignment3_2.html',
                                       users_details=users_details)

            if email in emails:
                user_index = get_user_index_by_email(email)
                username = users_details[user_index]['name']
                user_password = users_details[user_index]['password']
                return render_template('assignment3_2.html',
                                       username=username,
                                       email=email,
                                       user_password=user_password)
            else:
                return render_template('assignment3_2.html',
                                       message='not found')
        else:
            return render_template('assignment3_2.html')


    #for log in
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_index = get_user_index_by_username(username)
        if username in usernames:
            pas_in_dict = users_details[user_index]['password']
            if pas_in_dict == password:
                session['username'] = username
                session['loggedin'] = True
                return render_template('assignment3_2.html',
                                       message='Logged in successfully!',
                                       username=username)
            else:
                return render_template('assignment3_2.html',
                                       message='Wrong password')
        else:
            return render_template('assignment3_2.html',
                                   message='Incorrect username')
    return render_template('assignment3_2.html')





# get all the user's emails and usernames list
emails =[]
for i in range(len(users_details)):
    emails.append(users_details[i]['email'])

usernames =[]
for i in range(len(users_details)):
    usernames.append(users_details[i]['name'])


# functions to get the user's index in the users' dict by email/username
def get_user_index_by_email(email):
    for i in range(len(users_details)):
        if users_details[i]['email'] == email:
            return i

def get_user_index_by_username(username):
    for i in range(len(users_details)):
        if users_details[i]['name'] == username:
            return i


@app.route("/logout/", methods=['POST'])
def log_out():
    session['loggedin'] = False
    session.clear()
    return redirect(url_for('assignment3_2_page'))


#dictionary of the session
@app.route('/session')
def session_func():
    return jsonify(dict(session))





if __name__ == '__main__':
    app.run(debug=True)


