
from afristyle import db

class User(db.Model):
    
  __tablename__ = 'user'
  
  username = db.Column(db.String(20),  primary_key=True,unique=True, nullable=False)
  password = db.Column(db.String(100))
  first_name = db.Column(db.String(50))
  last_name = db.Column(db.String(50))
  email = db.Column(db.String(50), unique=True, nullable=False)
  phone_number = db.Column(db.String(30), unique=True, nullable=False)
  role = db.Column(db.String(10))
  # articles = db.relationship('Article', backref='user') 