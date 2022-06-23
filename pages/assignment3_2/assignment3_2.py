from flask import Blueprint, render_template, redirect, url_for
from flask import request, session, jsonify
from utilities.db_manager import interact_db


#assignment3_2 blueprint definition
assignment3_2 = Blueprint('assignment3_2', __name__,
                          static_folder='static',
                          template_folder='templates')


#routes
@assignment3_2.route('/assignment3_2',  methods=['GET', 'POST'])
def assignment3_2_page():
    users_details_query = "select * from users"
    users_details = interact_db(users_details_query, query_type='fetch')
    emails_query = "select email from users"
    emails_list = interact_db(emails_query, query_type='fetch')
    emails = []

    for user in emails_list:
        emails.append(user.email)


    #for search
    if request.method == 'GET':
        if 'email' in request.args:
            email = request.args['email']

            #if no email - return all user's details
            if email == '':
                return render_template('assignment3_2.html',
                                       users_details=users_details)

            if email in emails:
                username = get_username_by_email(email)
                user_password = get_password_by_email(email)
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
        email = request.form['email']
        password = request.form['password']

        query = "select username from users"
        usernames = interact_db(query, query_type='fetch')

        usernames_list = interact_db(query, query_type='fetch')
        usernames = []

        for user in usernames_list:
            usernames.append(user.username)

        if email in emails:
            pas_in_dict = get_password_by_email(email)
            username_in_dict = get_username_by_email(email)

            if pas_in_dict == password:
                session['username'] = username_in_dict
                session['loggedin'] = True
                return render_template('assignment3_2.html',
                                       message='Logged in successfully!',
                                       username=username_in_dict)
            else:
                return render_template('assignment3_2.html',
                                       message='Wrong password')
        else:
            return render_template('assignment3_2.html',
                                   message='Incorrect email')
    return render_template('assignment3_2.html')




@assignment3_2.route("/logout/", methods=['POST'])
def log_out():
    session['loggedin'] = False
    session.clear()
    return redirect('/assignment3_2')





def get_username_by_email(email):
    query = "select username from users where email='%s';" % email
    usernames = interact_db(query, query_type='fetch')
    for user in usernames:
        username = user.username
    return username



def get_password_by_email(email):
    query = "select password from users where email='%s';" % email
    passwords = interact_db(query, query_type='fetch')
    for user in passwords:
        password = user.password
    return password




def get_username_by_email(email):
    query = "select username from users where email='%s';" % email
    usernames = interact_db(query, query_type='fetch')
    for user in usernames:
        username = user.username
    return username




