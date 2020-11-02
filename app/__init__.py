from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):


    #Initializing the application
    app = Flask(__name__)

    #Creating the app configurations
    app.config.from_object(config_options(config_name))

    # #Setting up the configurations
    # app.config.from_object(DevConfig)

    #Initializing Flask Extensions
    bootstrap.init_app(app)

    #Registering the Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from app import views
    from app import error

    return app