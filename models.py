from google.appengine.ext import db



class softwares(db.Model):
	person = db.StringProperty()
	name = db.StringProperty()
	version = db.StringProperty()
	platform = db.StringProperty()
	author = db.StringProperty()	
	url = db.StringProperty()
	date = db.DateTimeProperty(auto_now_add=True)
