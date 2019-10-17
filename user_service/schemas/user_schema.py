#!/usr/bin/env python3
from marshmallow import fields, post_load
import marshmallow.validate
from marshmallow_sqlalchemy import ModelSchema
from model import User
import marshmallow.validate

import string
import random
import hashlib


class UserSchema(ModelSchema):

    name = fields.String(validate=[marshmallow.validate.Length(min=3), marshmallow.validate.Regexp("^[a-z].[a-z0-9_]*$")], allow_none=False, required=True)
    # disabled =

    @post_load(pass_many=False)  # Autohash password on every load... altrought this is only usable for loading
    def password_hash(self, item, many, **kwargs):
        item.salt = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=8))  # TODO: configurable
        item.password = hashlib.sha512((item.password + item.salt).encode("utf-8")).hexdigest()  # TODO: could be faster if stored binary in db

        return item

    class Meta:
        exclude = ["id", "salt"]
        load_only = ["password"]
        dump_only = ["created"]
        model = User

