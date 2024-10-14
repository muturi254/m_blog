from flask import Flask

from config import Config


app = Flask(__name__)

# set configurations for flask
app.config.from_object(Config)

from app import routes
