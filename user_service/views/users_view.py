#!/usr/bin/env python3
from flask_classful import FlaskView
from flask import request, abort, jsonify
from flask_jwt_simple import jwt_required, get_jwt_identity
from marshmallow.exceptions import ValidationError

import sqlalchemy.exc

from utils import json_required
from schemas import UserSchema
from model import db, User

#
# This view handles user creating (registering), disabling, password update, etc.
# This path SHOULD NOT be exposed to users, as currently it requires no authentication
#


class UsersView(FlaskView):

    user_schema = UserSchema(many=False, session=db.session)
    user_update_schema = UserSchema(many=False, session=db.session, exclude=["name"])  # PATCHing username is not allowed
    users_schema = UserSchema(many=True)

    def index(self):  # list all users
        all_users = User.query.all()
        return jsonify(self.users_schema.dump(all_users))

    def get(self, username: str):  # get specific info

        u = User.query.find_by(name=username).first()

        if u:
            return jsonify(self.user_schema.dump(u))
        else:
            abort(404)

    @json_required
    def post(self):  # register user

        try:
            u = self.user_schema.load(request.get_json())
        except ValidationError as e:
            abort(422, str(e))

        db.session.add(u)

        try:
            db.session.commit()  # save updated userinfo
        except sqlalchemy.exc.IntegrityError as e:
            abort(409, "Database integrity violation (username already taken?)")

        return jsonify(self.user_schema.dump(u))

    @json_required
    def patch(self, username: str):  # update user info

        u = User.query.filter_by(name=username).first()

        if not u:
            abort(404)

        try:
            self.user_update_schema.load(request.get_json(), instance=u, partial=True)
        except ValidationError as e:
            if "name" in e.data:
                abort(403, "Username can not be changed")
            else:
                abort(422, str(e))

        db.session.commit()  # save updated userinfo

        return jsonify(self.user_schema.dump(u))
