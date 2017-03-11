# from flask import Flask, render_template
# from flask import request
# from flask_bootstrap import Bootstrap
# from flask_moment import Moment
# from datetime import datetime
# from flask_wtf import Form
# from wtforms import StringField, SubmitField
# from wtforms.validators import Required
#
#
# app = Flask(__name__)
# bootstrap = Bootstrap(app)
# moment = Moment(app)
# app.config['SECRET_KEY'] = 'CREATETHISSOMETHINGGOOD'
#
#
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#  name = None
#  form = NameForm()
#  if form.validate_on_submit():
#     name = form.name.data
#     form.name.data = ''
#  return render_template('index.html', form=form, name=name)
#
#
#
# @app.route('/user/<name>')
# def user(name):
#  return '<h1>Hello, %s!</h1>' % name
#
#
#
#
#
#
#
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500
#
#
#
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
