from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin
import warnings

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Adminka
########
import flaskblog.admin as views
from flask_admin.contrib.sqla import ModelView

# admin = Admin(app)
# admin = Admin(app, name='app',
# template_mode='bootstrap3', index_view=views.MyAdminIndexView(name = 'StartAdminPage'))

admin = Admin(app, name='app', index_view=views.MyAdminIndexView(name='StartAdminPage'))

with warnings.catch_warnings():
    warnings.filterwarnings('ignore', 'Fields missing from ruleset', UserWarning)
    admin.add_view(views.HelloView(name='Hello'))
    admin.add_view(views.UserAdminView(views.User, db.session))
########

from flaskblog import routes
