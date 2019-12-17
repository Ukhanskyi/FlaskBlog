import os
import warnings

from flask import Flask, Blueprint
from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
bp = Blueprint('api', __name__)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

app.config['CKEDITOR_PKG_TYPE'] = 'basic'
ckeditor = CKEditor(app)

# ################################# Admin Panel ###################################

import flaskblog.admin as views

admin = Admin(app, name='app', index_view=views.MyAdminIndexView(name='AdminPage'))

with warnings.catch_warnings():
    warnings.filterwarnings('ignore', 'Fields missing from ruleset', UserWarning)
    admin.add_view(views.UserAdminView(views.User, db.session))


from flaskblog import routes
