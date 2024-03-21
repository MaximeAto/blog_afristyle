from flask import Blueprint, render_template


user = Blueprint('user', __name__)

@user.route("/connexion")
def home():
    return render_template("index.html")

@user.route("/liste")
def register():
    return render_template("login/register.html")
