from flask import Flask,render_template,session,url_for,redirect,request
from models import *
import os
from blueprints import *
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin as ad

class Myapp:
	app = Flask(__name__)
	app.register_blueprint(pages.page)
	app.register_blueprint(Blog.blog)
	app.register_blueprint(Auth.auth)
	app.register_blueprint(Admin.central)

	app.secret_key= os.urandom(64)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databse.db'
	db.init_app(app)
	admin_view = ad(app, name='control', template_mode='bootstrap3')

	# Create view classes for each model
	class UsersView(ModelView):
	    column_list = ['id', 'name', 'email', 'password']
	class MessageView(ModelView):
	    column_list = ['id', 'name', 'email', 'body']
	class BlogView(ModelView):
		column_list = ['id','blog id','title','title2','image','date','body']
	

	# Register the views for each model with the Flask-Admin instance
	admin_view.add_view(UsersView(Users, db.session))
	admin_view.add_view(MessageView(Messages, db.session))
	admin_view.add_view(BlogView(BlogPosts,db.session))
	
	with app.app_context():
		db.create_all()
	@app.route('/')
	def index():
		return redirect(url_for('home.index'))
	@app.route('/contactus',methods= ['GET','POST'])
	def contact():
		if request.method == 'POST':
			name = request.form.get('name')
			email = request.form.get('email')
			body = request.form.get('body')
			new_message = Messages(name,email,body)
			db.session.add(new_message)
			db.session.commit()
			return redirect(url_for('home.index'))
	@app.route('/subscribe',methods = ['GET','POST'])
	def subscribe():
		if request.method == 'POST':
			email = request.form.get('name')
			date = time.ctime()
			new_sub = Sub(email,date)
			db.session.add(new_sub)
			db.session.close()
			return redirect(url_for('home.index'))