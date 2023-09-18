from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Users(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(100),unique = True)
	email = db.Column(db.String(200))
	password = db.Column(db.String(1000))
	def __init__(self,username,email,password):
		self.username = username
		self.email = email
		self.password = password
	def data(self):
		return [self.username,self.email,self.password]
class Messages(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String(200))
	email = db.Column(db.String(200))
	body = db.Column(db.String(1200))
	def __init__(self,name,email,body):
		self.username = name
		self.email = email
		self.body = body
	def data(self):
		return [self.name,self.email,self.body]
class BlogPosts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.String(50), unique=True, nullable=False)  # Unique identifier for each blog post
    title = db.Column(db.String(200), nullable=False)
    title2 = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(50), nullable=False)  # Date field to store the publication date
    body = db.Column(db.Text, nullable=False)
    

    def __init__(self, blog_id, title,title2,image, date ,body):
        self.blog_id = blog_id
        self.title = title
        self.title2 = title2
        self.image = image
        self.date = date
        self.body = body
        

    def data(self):
        return [self.blog_id, self.title, self.title2,self.image, self.date, self.body]
class Sub(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user = db.Column(db.String(200), unique=True, nullable=False)
	date = db.Column(db.String(200))
	def __init__(self,user,date):
		self.user = user
		self.date = date
	def data(self):
		return [self.user,self.data]





