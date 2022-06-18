from flask import Blueprint, render_template
from flask import request, session, jsonify


#assignment3_2 blueprint definition
assignment3_2 = Blueprint('assignment3_2', __name__,
                          static_folder='static',
                          template_folder='templates')

#
# #routes
# @assignment3_2.route('/assignment3_2',  methods=['GET', 'POST'])
#  def assignment3_2_page():
#
#
#      #for search
#      if request.method == 'GET':
#          if 'email' in request.args:
#              email = request.args['email']
#
#              if email == '':
#                  return render_template('assignment3_2.html',
#                                         users_details=users_details)
#
#              if email in emails:
#                  user_index = get_user_index_by_email(email)
#                  username = users_details[user_index]['name']
#                  user_password = users_details[user_index]['password']
#                  return render_template('assignment3_2.html',
#                                         username=username,
#                                         email=email,
#                                         user_password=user_password)
#              else:
#                  return render_template('assignment3_2.html',
#                                         message='not found')
#          else:
#              return render_template('assignment3_2.html')
#
#
#      #for log in
#      if request.method == 'POST':
#          username = request.form['username']
#          password = request.form['password']
#          user_index = get_user_index_by_username(username)
#          if username in usernames:
#              pas_in_dict = users_details[user_index]['password']
#              if pas_in_dict == password:
#                  session['username'] = username
#                  session['loggedin'] = True
#                  return render_template('assignment3_2.html',
#                                         message='Logged in successfully!',
#                                         username=username)
#              else:
#                  return render_template('assignment3_2.html',
#                                         message='Wrong password')
#          else:
#              return render_template('assignment3_2.html',
#                                     message='Incorrect username')
#      return render_template('assignment3_2.html')
#
#

