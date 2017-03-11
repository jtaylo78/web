from datetime import datetime
from flask import render_template, session, redirect, url_for
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import MySQLdb
from flask import current_app, render_template


from . import main
#from . import NameForm
from .. import db
from ..models import User
@main.route('/', methods=['GET', 'POST'])
def index():
     form = NameForm()
     if form.validate_on_submit():
     # ...
        return redirect(url_for('.index'))
     return render_template('index.html',
             form=form, name=session.get('name'),
             known=session.get('known', False),
             current_time=datetime.utcnow())

@main.route('/search', methods=['GET', 'POST'])
def search_main():
     form = SearchForm()
     search_string = None
     if form.validate_on_submit():
        session['search_string'] = form.search.data
        #session['search_data']
        getFullTextData('cmd')
        return redirect(url_for('.search_main'))
     return render_template('search.html',
             form=form, search_string=session.get('search_string'),
             known=session.get('known', False),
             current_time=datetime.utcnow())


def getFullTextData(search_string):
    app = current_app._get_current_object()
    db = MySQLdb.connect(host=app.config['SPHINX_SERVER'],port=app.config['SPHINX_PORT'])

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT * from test1")

class NameForm(Form):
 name = StringField('What is your name?', validators=[Required()])
 submit = SubmitField('Submit')

class SearchForm(Form):
 search = StringField('Search', validators=[Required()])
 submit = SubmitField('Submit')