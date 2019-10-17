#!/usr/bin/env python3
from flask import Flask
from flask_jwt_simple import JWTManager
from datetime import timedelta
import os


# import stuff
from model import db
from utils import register_all_error_handlers

# import views
from views import TokenView

import configuration

# create flask app
app = Flask(__name__)

# configure flask app
app.config['SQLALCHEMY_DATABASE_URI'] = configuration.SQLALCHEMY_DB_URI
app.config['JWT_PRIVATE_KEY'] = configuration.JWT_PRIVATE_KEY
app.config['JWT_PUBLIC_KEY'] = configuration.JWT_PUBLIC_KEY

app.config['JWT_ALGORITHM'] = 'RS512'
app.config['JWT_EXPIRES'] = timedelta(hours=2)  # yup, that long

# initialize stuff
db.init_app(app)
jwt = JWTManager(app)


with app.app_context():
    db.create_all()

# register error handlers
register_all_error_handlers(app)

# register views
for view in [TokenView]:
    view.register(app, trailing_slash=False)

# start debuggig if needed
if __name__ == "__main__":
    app.run(debug=True)
