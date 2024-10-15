from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config


app = Flask(__name__)

# set configurations for flask
app.config.from_object(Config)

# db confs
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# login manager confs
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
