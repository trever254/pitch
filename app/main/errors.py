from flask import render_template
from . import main

@main.app__errorhandler(404) 
def four_Ow_four(erxror):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404