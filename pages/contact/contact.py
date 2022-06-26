import express as express
from flask import Blueprint, render_template, request, flash, redirect, jsonify

from utilities.db_manager import interact_db

times = 0
is_contact = 0

#assignment3_1 blueprint definition
contact = Blueprint('contact', __name__,
                    static_folder='static',
                    static_url_path='/contact',
                    template_folder='templates')

#routes
@contact.route('/contact', methods=['GET', 'POST'])
def contact_page():
    return render_template('contact.html')



@contact.route('/create_inquire', methods=['GET', 'POST'])
def create_inquire():
    username = request.form['username']
    email = request.form['email']
    phone = request.form['phone']
    range = request.form['range']
    text = request.form['text']

    query = "insert into contact(name, email, phone_num, rate, content) values ('%s','%s','%s','%s','%s')" % (username, email, phone, range, text)

    interact_db(query, query_type='commit')
    flash('Contact Sent Successfully!', 'success')

    return redirect('/contact')


