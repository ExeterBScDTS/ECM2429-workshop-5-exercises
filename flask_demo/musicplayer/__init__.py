import os

from flask import Flask, Response
import logging

logging.basicConfig(level=logging.DEBUG)

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # apply the blueprints to the app
    from musicplayer import page
    app.register_blueprint(page.bp) 
    app.add_url_rule("/", endpoint="index")

    # audio streaming
    @app.route("/music/<path:tune>")
    def streamwav(tune):
        """ Stream WAV audio.
        To stream other formats the code required in the same,
        just be sure to set the correct mimetype in Respose.
        e.g. "audio/ogg"
        """
        logging.debug(f"streaming:{tune}")
        def generate():
            with open("Beethoven5.wav", "rb") as fwav:
                data = fwav.read(1024)
                while data:
                    yield data
                    data = fwav.read(1024)
        return Response(generate(), mimetype="audio/x-wav")
   
    return app
