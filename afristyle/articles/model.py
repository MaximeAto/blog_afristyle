from datetime import datetime
from afristyle import db

class Article(db.Model):
    
  __tablename__ = 'article'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  titre = db.Column(db.String(100))
  contenu = db.Column(db.Text)
  date_publication = db.Column(db.DateTime, default=datetime.now)
  auteur = db.Column(db.String(50))
  description = db.Column(db.String(255), nullable=False)
  categorie = db.Column(db.String(50), nullable=False)
  image_principale = db.Column(db.String(50), nullable=False)
  # id_user = db.Column(db.String(20), db.ForeignKey('user.username'), nullable=False) 