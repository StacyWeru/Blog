from flask import render_template,url_for
from app import app

#views
@app.route('/')
def index():
    '''
    View root page returns the index page
    '''

    return render_template('index.html')