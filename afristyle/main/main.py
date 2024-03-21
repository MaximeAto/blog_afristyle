from flask import Blueprint, render_template

from afristyle.articles.model import Article
from afristyle.articles.mashmallw import Mashmallow


main = Blueprint('main', __name__)

@main.route("/")
@main.route("/index")
def home():
    # Récupérer les 6 premiers articles triés par date de création décroissante
    articles = Article.query.order_by(Article.date_publication.desc()).limit(9).all()
    
    mashmallow_article = Mashmallow(many=True)
    article_data = mashmallow_article.dump(articles)
    
    if(len(article_data)):
         return render_template("index.html", articles = article_data )
    else:
         return render_template("index.html")

@main.route("/register")
def register():
    return render_template("login/register.html")
