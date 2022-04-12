# __init__.py
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
app = Flask(__name__)
app.secret_key = "shhhhhh"
bcrypt = Bcrypt(app)
DB = 'ding'
cors = CORS(app, supports_credentials=True)
