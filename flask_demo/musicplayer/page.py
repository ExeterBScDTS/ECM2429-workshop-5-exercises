from flask import Blueprint
from flask import render_template
from flask import request
import logging

bp = Blueprint("page", __name__)

@bp.route("/")
def index():
    albums = [{"id": 0, "title": "never mind"}, {"id": 1, "title": "manifesto"}]

    tracks = [{"id": "n/n1", "title": "n1"}, {"id": "n/n2", "title": "n2"}]

    album_id = request.args.get('a')
    # album_id will be None, a valid id, or an invalid id (perhaps something the user made up)

    logging.debug(f"album_id={album_id}")
    return render_template("page/index.html", albums=albums, tracks=tracks)
