#!/usr/bin/env python3
from flask_classful import FlaskView
from flask import request, abort
from flask_jwt_simple import create_jwt, jwt_required, get_jwt_identity
from marshmallow.exceptions import ValidationError

from sqlalchemy import text

from utils import json_required
from schemas import RequestSchema
from model import User


class TokenView(FlaskView):

    request_schema = RequestSchema(partial=False)

    @jwt_required
    def get(self):  # Testing the token
        return {"username": get_jwt_identity()}

    @json_required
    def post(self):
        try:
            credentials = self.request_schema.load(request.get_json())
        except ValidationError:
            abort(422)

        u = User.query.from_statement(text("SELECT * FROM user WHERE password = SHA2(CONCAT(:p, user.salt), 512) AND name = :n")).params(p=credentials['password'], n=credentials['username']).first()

        if u:
            return {'token': create_jwt(u.name)}
        else:
            abort(401)
