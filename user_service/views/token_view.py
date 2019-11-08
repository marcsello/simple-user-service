#!/usr/bin/env python3
from flask_classful import FlaskView
from flask import request, abort, current_app
from flask_jwt_simple import create_jwt, jwt_required, get_jwt_identity
from marshmallow.exceptions import ValidationError

from sqlalchemy import text
import sqlalchemy.exc

from utils import json_required
from schemas import TokenRequestSchema
from model import User

import hashlib

#
# This view handles token issuing for certain users.
# This path MIGHT be exposed to users, but be very careful
#


class TokenView(FlaskView):

    request_schema = TokenRequestSchema(partial=False)

    @json_required
    def post(self):
        try:
            credentials = self.request_schema.load(request.get_json())
        except ValidationError:
            abort(422)

        u = None
        try:
            u = User.query.from_statement(text("SELECT * FROM users WHERE password = SHA2(CONCAT(:p, users.salt), 512) AND name = :n AND NOT disabled")).params(p=credentials['password'], n=credentials['name']).first()
        except sqlalchemy.exc.OperationalError:
            # Magic login failed... attempting a less secure login
            current_app.logger.warning("Secure validation (inside the database) is not possible. Attempting a less secure validation... PLS FIX!")

            u = User.query.filter_by(name=credentials['name']).first()

            if u:

                hash = hashlib.sha512((credentials['password'] + u.salt).encode("utf-8")).hexdigest()

                if u.password != hash:
                    del u
                    u = None




        if u:
            current_app.logger.info("%s logged in successfully",u.name)
            return {'token': create_jwt(u.name)}
        else:
            current_app.logger.info("Login failed for %s",credentials['name'])
            abort(401)
