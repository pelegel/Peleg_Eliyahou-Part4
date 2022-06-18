from flask import Blueprint, render_template

#assignment3_1 blueprint definition
assignment3_1 = Blueprint('assignment3_1', __name__,
                          static_folder='static',
                          static_url_path='/pages/assignment3_1',
                          template_folder='templates')

#routes
@assignment3_1.route('/assignment3_1')
def assignment3_1_page():
    artists = {'maroon 5': 'Band', 'justin bieber': 'Male singer', 'taylor swift': 'female Singer',
               'Lady gaga': 'Female Singer', 'noa kiler': 'Female Singer'}
    females = []
    males = []
    bands = []
    return render_template('assignment3_1.html', artists=artists, females=females, males=males, bands=bands)
