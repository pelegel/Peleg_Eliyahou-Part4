import express as express
from flask import Blueprint, render_template, request, flash, redirect, jsonify

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





