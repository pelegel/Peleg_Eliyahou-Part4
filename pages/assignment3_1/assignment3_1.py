from flask import Blueprint, render_template, request, flash, redirect

#assignment3_1 blueprint definition
from utilities.db_manager import interact_db

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




#------------- Insert Recommendation  ---------------
@assignment3_1.route('/share_recommendation', methods=['POST'])
def share_recommendation_func():
    artist_name = request.form['artist'].title()
    artist_type = request.form['artistType'].title()

    query = "select artist from Recommendations"
    artists_list = interact_db(query, query_type='fetch')
    artists = []
    for artist in artists_list:
        artists.append(artist.artist)
    print(artists)

    if artist_name in artists:
        flash('Insertion Warning: This artist is already in our recommendations', 'danger')

    elif artist_type != "Band" and artist_type != "Male Singer" and artist_type != "Female Singer":
        flash('Insertion Warning: Artist Type must be: Band/ Male Singer/ Female Singer', 'danger')

    #create recommendation
    else:
        query_rec = "insert into Recommendations(Artist, Type) values ('%s','%s')" % (artist_name, artist_type)
        interact_db(query_rec, query_type='commit')
        flash('Your recommendation was sent successfully! Our team will check it out and hopefully will add it to our professional recommendations', 'success')

    return redirect('/assignment3_1')


