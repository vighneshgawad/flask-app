from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flaskapp.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view='users.login'
login_manager.login_message_category = 'info'

mail = Mail(app)
moment = Moment(app)
migrate = Migrate(app, db)

from flaskapp.users.routes import users
from flaskapp.posts.routes import posts
from flaskapp.main.routes import main
from flaskapp.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)


