from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_login import LoginManager

DATABASE = SQLAlchemy()
CACHE= Cache()
LOGIN_MANAGER= LoginManager()