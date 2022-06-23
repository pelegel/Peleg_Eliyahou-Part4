from flask import render_template, redirect, url_for, flash
from flask import Blueprint, request, session, jsonify, json
from utilities.db_manager import interact_db
import requests


#assignment3_1 blueprint definition
assignment4 = Blueprint('assignment4', __name__,
                        static_folder='static',
                        static_url_path='/assignment4',
                        template_folder='templates')


#routes
@assignment4.route('/assignment4')
def assignment4_page():
    session['searched_user'] = ''
    return render_template('assignment4.html')


@assignment4.route('/assignment4/outer_source')
def outer_source_func():
    session['searched_user'] = ''
    return render_template('assignment4_outer_source.html')

# ------------- directly to json ---------------
# @assignment4.route('/assignment4/users')
# def assignment4_users_page():
#     return redirect(url_for('assignment4.get_users_in_json'))

#------------- users page navigating to json ---------------
@assignment4.route('/assignment4/userss')
def assignment4_userss_page():
    return render_template('assignment4_users.html')







#---------------------------------------------- ASSIGNMENT 4 - Part A --------------------------------------------------

#------------- Select All Users ---------------
@assignment4.route('/select_users')
def select_users():
    query = "select * from users"
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment4.html', users=users_list)



#------------- Delete User ---------------
@assignment4.route('/delete_user', methods=['POST'])
def delete_user():
    email = request.form['email']

    #email not provided
    if email == "":
        flash('Deletion Warning: No email for deletion was provided', 'warning')

    #email provided
    else:
        # get emails list to check if exists
        query = "select email from users"
        emails_list = interact_db(query, query_type='fetch')
        emails = []

        for user in emails_list:
            emails.append(user.email)

        # user exists
        if email in emails:
            query = "delete from users where email='%s';" % email
            interact_db(query, query_type='commit')
            flash('User Deleted Successfully!', 'success ')

        # no such user
        else:
            flash('Deletion Failed: There is no such user with the provided email', 'danger')

    return redirect('/assignment4')



#------------- Insert User ---------------
@assignment4.route('/insert_user', methods=['POST'])
def insert_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    #not all details was provided
    if username == "" or email == "" or password == "":
        flash('Insertion Warning: Please fill all the user details', 'warning')

    #password too short
    elif len(password) < 8:
        flash('Insertion Warning: Password must contain at least 8 characters', 'warning')

    #create user
    else:
        query = "insert into users(username, email, password) values ('%s','%s','%s')" % (username, email, password)
        interact_db(query, query_type='commit')
        flash('User Inserted Successfully!', 'success')

    return redirect('/assignment4')



#------------- Update User ---------------
@assignment4.route('/update_user', methods=['POST'])
def update_user():
    email_to_update = request.form['email_to_update']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    #get emails list to check if exists
    emails_query = "select email from users"
    emails_list = interact_db(emails_query, query_type='fetch')
    emails = []
    for user in emails_list:
        emails.append(user.email)


    #email not provided
    if email_to_update == "":
        flash('Update Warning: No user email was provided for update', 'warning')

    #no such user
    elif email_to_update not in emails:
        flash('Update Failed: There is no such user with the provided email', 'danger')

    #no update details provided
    elif username == "" and email == "" and password == "":
        flash('Update Warning: Please fill at least one field to update', 'warning')

    #update only the provided field
    else:
        if username != "":
            query = "update users set username='%s' where email='%s';" % (username, email_to_update)
            interact_db(query, query_type='commit')

        if password != "":
            query = "update users set password='%s' where email='%s';" % (password, email_to_update)
            interact_db(query, query_type='commit')

        if email != "":
            query = "update users set email='%s' where email='%s';" % (email, email_to_update)
            interact_db(query, query_type='commit')

        flash('User Updated Successfully!', 'success')

    return redirect('/assignment4')




#---------------------------------------------- ASSIGNMENT 4 - Part B --------------------------------------------------

#--------------------------------------------- ASSIGNMENT 4B - USERS ---------------------------------------------------

# ---------- JSON -------------
@assignment4.route('/assignment4/users')
def get_users_in_json():
    query = "select * from users"
    users_list = interact_db(query, query_type='fetch')
    users_dict = {}
    i = 0
    for user in users_list:
        i += 1
        user_dict = {}
        user_dict['email'] = user.email
        user_dict['username'] = user.username
        user_dict['password'] = user.password
        users_dict[i] = user_dict
    return jsonify(users_dict)




#------------------------------------------ ASSIGNMENT 4B - OUTER SOURCE -----------------------------------------------


# ---------- Front-End -------------

@assignment4.route('/fetch_fe')
def fetch_fe_func():
    if 'type' in request.args:
        user_id = int(request.args['user_num_fetch_fe'])
        if request.args['type'] == 'sync':
            users = []
            for i in range(user_id):
                res = requests.get(f'https://reqres.in/api/users/{id}')
                users.append(res.json())
            session['user_id_fe'] = user_id
    return render_template('assignment4_outer_source.html')





# ---------- Back-End -------------

@assignment4.route('/fetch_be')
def fetch_be_func():
    session['searched_user'] = ''

    if 'type' in request.args:
        user_id = int(request.args['user_num_fetch_be'])
        users = []

        # SYNC
        if request.args['type'] == 'sync':
            res = requests.get(f'https://reqres.in/api/users')
            users_data = res.json()
            user = users_data['data']
            users.append(user)
        save_users_to_session(users, user_id)

    else:
        session['searched_user'] = ''

    return render_template('assignment4_outer_source.html')


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

    session['searched_user'] = user_to_save






#---------------------------------------------- ASSIGNMENT 4 - Part C --------------------------------------------------

@assignment4.route('/assignment4/restapi_users/', defaults={'user_id': -1})
@assignment4.route('/assignment4/restapi_users/<int:user_id>')
def get_users_restapi_func(user_id):
    if user_id == -1:
        return_dict = {}
        query = 'select * from users limit 1;'
        users = interact_db(query=query, query_type='fetch')
        return_dict = {
            'status': 'success',
            'id': users[0].user_id,
            'name': users[0].username,
            'email': users[0].email,
            'password': users[0].password
        }
    else:
        query = 'select * from users where user_id=%s;' % user_id
        users = interact_db(query=query, query_type='fetch')
        # print(type(user_id))
        if len(users) == 0:
            return_dict = {
                'status': 'failed',
                'message': 'user not found'
            }
        else:
            return_dict = {
                'status': 'success',
                'id': users[0].user_id,
                'name': users[0].username,
                'email': users[0].email,
                'password': users[0].password
            }
    return jsonify(return_dict)


