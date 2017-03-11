from datetime import datetime
from flask import render_template, session, redirect, url_for
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


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
     if form.validate_on_submit():
     # ...
        return redirect(url_for('.search_main'))
     return render_template('search.html',
             form=form, name=session.get('name'),
             known=session.get('known', False),
             current_time=datetime.utcnow())



class NameForm(Form):
 name = StringField('What is your name?', validators=[Required()])
 submit = SubmitField('Submit')

class SearchForm(Form):
 search = StringField('Search', validators=[Required()])
 submit = SubmitField('Submit')