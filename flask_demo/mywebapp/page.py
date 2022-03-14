from flask import Blueprint
from flask import render_template

bp = Blueprint("page", __name__)

@bp.route("/")
def index():
    return render_template("page/index.html")
