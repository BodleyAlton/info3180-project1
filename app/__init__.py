from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://proj1:P@ssw0rd@localhost/profiles"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['ALLOWED_EXTENSIONS'] = "set(['png', 'jpg', 'jpeg', 'gif'])"
app.config['UPLOAD_FOLDER']= "./app/static/uploads"

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# app.config.from_object(__name__)
from app import views