# Flask demo

## My Web App (mywebapp)

A simple flask demo with static files and templates.

Requires flask.  Install using pip, prefereably in a virtual env.

```sh
> pip install flask
```

To run type ```run_mywebapp.bat```   (or ./run_mywebapp.sh on Mac)
```sh
> cd flask_demo
> set FLASK_APP=mywebapp
> set FLASK_ENV=development
> flask run
```

## MusicPlayer

A first iteration of a music streaming app.

To run type ```run_musicplayer.bat```   (or ./run_musicplayer.sh on Mac)
```sh
> cd flask_demo
> set FLASK_APP=musicplayer
> set FLASK_ENV=development
> flask run
```

## The Flask Tutorial

Follow the instructions here -

<https://flask.palletsprojects.com/en/2.0.x/tutorial/>


N.B.  You might need to install wheel first.

```sh
pip install wheel
```

### Important

The tutorial instructions install the tutorial application in a virtual environment as a module called **flaskr**, so you must first create a virtual environment. 


### To run

If you just want to run the tutorial example, the code is included here in the tutorial folder.

```sh
> cd tutorial
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask init-db
> flask run
```

### Repository

<https://github.com/pallets/flask/tree/2.0.3/examples/tutorial>



