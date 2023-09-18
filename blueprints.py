import bleach
from flask import render_template,session,url_for,redirect,Blueprint,request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from decorators import *
from models import *
from flask_bcrypt import Bcrypt
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary
import os
import time
from tags import html_tags

# Initialize Cloudinary
cloudinary.config(
    cloud_name='dvnflgqs2',
    api_key='975551641336967',
    api_secret='l12W5dcvd3JvHDr7Hi-Wyx9Q17c'
)

bcrypt = Bcrypt()
class pages:
	page = Blueprint('home',__name__,url_prefix = '/home')
	@page.route('/')
	def index():
		return render_template('index.html')
class Auth:
	auth = Blueprint('auth',__name__,url_prefix = '/auth')
	@auth.route('/login')
	def login():
		return render_template('login.html')
	@auth.route('/signup')
	def signup():
		return render_template('signup.html')
	@auth.route('signup/confirm_signup',methods = ['GET','POST'])
	def confirm_signup():
		if request.method == 'POST':
			username =request.form.get('username')
			email = request.form.get('email')
			password = bcrypt.generate_password_hash(request.form.get('password'))
			new_user = Users(username,email,password)
			db.session.add(new_user)
			db.session.commit()
			session['username'] = username
			return redirect(url_for('blog.index'))
	@auth.route('login/confirm_login',methods = ['GET','POST'])
	def confirm_login():
		username = request.form.get('username')
		password = request.form.get('password')
		if request.method == 'POST':
			user = Users.query.filter_by(username= username).first()
			if not user:
				return 'No such user'
			elif not bcrypt.check_password_hash(user.data()[2],password):
				return 'Invalid Password'
			else:
				session['username'] = username
				return redirect(url_for('blog.index'))

	@auth.route('/logout')
	def logout():
		session.pop('username')
		return redirect(url_for('home.index'))
class Blog:
	blog = Blueprint('blog',__name__,url_prefix = '/blog')
	@blog.route('/')
	@user.login_required
	def index():
		main = []
		data = BlogPosts.query.all()
		for it in data:
			main.append(it.data())
		print(main)
		return render_template('blog.html',blog = main)
class Admin:
	central = Blueprint('central',__name__,url_prefix = '/central')
	@central.route('/new_posts')
	def new():
		return render_template('newblog.html')
	@central.route('/create_post', methods=['POST'])
	def create_post():
	    if request.method == 'POST':
	        title = request.form['title']
	        title2 = request.form['title2']
	        body = request.form['body']
	        # Handle image upload to Cloudinary
	        uploaded_image = request.files['image']
	        blog_id = os.urandom(16)
	        date = time.ctime()
	        if uploaded_image:
	            result = upload(uploaded_image)
	            image_url, options = cloudinary_url(result['public_id'], format="jpg")
	        else:
	            # If no image is uploaded, set a default image URL or handle it as you prefer
	            image_url = 'https://example.com/default-image.jpg'
	        new = BlogPosts(blog_id, title,title2, image_url, date ,body)
	        db.session.add(new)
	        db.session.commit()

	        return render_template('blog.html',blog = body)
	
	

