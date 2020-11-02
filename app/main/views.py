from flask import render_template,url_for,request,redirect
from . import main


#views
@main.route('/')
def index():
    '''
    View root page returns the index page
    '''

    return render_template('index.html')