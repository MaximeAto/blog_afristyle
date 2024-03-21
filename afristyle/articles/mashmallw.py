from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from afristyle.articles.model import Article
from afristyle import ma

class Mashmallow(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Article