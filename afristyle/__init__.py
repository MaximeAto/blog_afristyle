from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from afristyle import config
from flask import Flask
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()

def create_app():
  
  app = Flask(__name__, template_folder='templates', static_folder='static')
  CORS(app)
  
  db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': '10322',
    'database': 'blogBd',
    'port': '5432'
  }
  
  # Connexion distante
  # db_config = {
  #     'host': 'dpg-cnu9jf0cmk4c7394olm0-a.frankfurt-postgres.render.com',
  #     'user': 'blogbd_gcvp_user',
  #     'password': 'xQl9c2gWB0JWtNAahNOpV7XRqUIDbvUA',
  #     'database': 'blogbd_gcvp',
  #     'port': '5432'
  # }
  
  # db_config = {
  #   'host': 'localhost',
  #   'user': 'root',
  #   'password': '',
  #   'database': 'blogbd',
  # }

  app.config['SECRET_KEY'] = config.SECRET_KEY
  #Charger les configurations à partir de l'objet config
  app.config.from_object(config)
  app.config['imagesPath'] = 'afristyle/static/images'

  # app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"
  app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
  
  # Initialiser la base de données
  db.init_app(app)
  ma.init_app(app)
  
  with app.app_context():
    
    
    from afristyle.main.main import main
    from afristyle.articles.routes import article
    from afristyle.utilisateur.routes import user
    from afristyle.categories.routes import category
    
    app.register_blueprint(main)
    app.register_blueprint(article)
    app.register_blueprint(user)
    app.register_blueprint(category)
    
    db.create_all()
    
  return app 