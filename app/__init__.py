from flask import Flask
from flask_bootstrap import Bootstrap

#Initializing the application
app = Flask(__name__)

#Setting up the configurations
app.config.from_object(DevConfig)

#Initializing Flask Extensions
bootstrap = Bootstrap(app)


from app import views
from app import error