#!/usr/bin/env python3
from flask_classful import FlaskView
from flask import request, abort
from flask_jwt_simple import jwt_required, get_jwt_identity
from marshmallow.exceptions import ValidationError

from sqlalchemy import text

from utils import json_required
from schemas import UserSchema
from model import db, User

#
# This view handles user creating (registering), disabling, password update, etc.
#


class UsersView(FlaskView):
    pass
