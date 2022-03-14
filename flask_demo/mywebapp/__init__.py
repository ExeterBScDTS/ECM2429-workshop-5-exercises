import os

from flask import Flask

from datetime import datetime


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # apply the blueprints to the app
    from mywebapp import page
    app.register_blueprint(page.bp) 

    app.add_url_rule("/", endpoint="index")


    # Can add other, non-blueprint, routes like this.
    @app.route("/date/")
    def date():
        return("<h1>" + str(datetime.now()) + "</h1>")

    @app.route("/hello/")
    def hello():
        # Could return text here, plain, or HTML, e.g.
        #  return "Hello, World!"
        # Or return some data from a file or stream, e.g.
        # return open("mywebapp/static/hello.html", "r").read()
        # If the file is in the static folder, this is better,
        # but not necessary as route /static/hello.html is
        # defined by default.
        return app.send_static_file("hello.html")

    return app
