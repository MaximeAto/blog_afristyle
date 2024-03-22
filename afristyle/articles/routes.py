import os
from flask import Blueprint, app, render_template, current_app
from flask import request
from afristyle import db
from afristyle.articles import Article
from flask import jsonify
from afristyle.articles.mashmallw import Mashmallow
from sqlalchemy.exc import SQLAlchemyError



article = Blueprint('article', __name__)

@article.route("/article/<article_id>", methods=["GET"])
def getarticle(article_id):
    try:
        article = Article.query.filter_by(id=article_id).first()
        if article_id:
            article_mash = Mashmallow(many=False)
            article_data = article_mash.dump(article)
            return render_template("article.html", article_data=article_data)
        else:
            return jsonify(message = 'article introuvable')
    except SQLAlchemyError as e :
       return jsonify(message='erreur lors du traitement de votre requête')
    

@article.route("/nouvelle_article")
def redaction():
    return render_template("redaction.html")

@article.route("/savearticle", methods=["POST"])
def savearticle():
  category = request.form.get('category')
  title = request.form.get('title')
  description = request.form.get('description')
  filename = request.form.get('path')
  contenu = request.form.get('contenu')
  image = request.files['image']

  # Create a new Article instance
  article = Article(
      categorie=category,
      titre=title,
      contenu=contenu,
      image_principale=filename,
      description = description
  )

  # Save the article to the database
  db.session.add(article)
  db.session.commit()
  
  # Save the image to the specified path
  images_path = current_app.config['imagesPath']
  image.save(os.path.join(images_path, filename))


  return jsonify(message= "Article enregistré avec succès!")


@article.route("/delete/<int:article_id>", methods=["DELETE"])
def delete_article(article_id):
    try:
        article = Article.query.get(article_id)
        if article:
            db.session.delete(article)
            db.session.commit()
            return jsonify(message="Article deleted successfully"), 200
        else:
            return jsonify(message="Article not found"), 404
    except Exception as e:
        return jsonify(message="Error deleting article: " + str(e)), 500
