from flask import Blueprint, render_template
from afristyle.articles.mashmallw import Mashmallow
from afristyle.articles.model import Article



category = Blueprint('category', __name__)

@category.route("/article_by_category/<category>")
def article_by_category(category):
  # Récupérer les 6 premiers articles triés par date de création décroissante
  articles = Article.query.order_by(Article.date_publication.desc()).all()
  
  mashmallow_article = Mashmallow(many=True)
  article_data = mashmallow_article.dump(articles)
  
  return render_template("category.html", articles = article_data , categorie= category )

