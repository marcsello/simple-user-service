#!/usr/bin/env python3
from .db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)

    name = db.Column(db.String(128), unique=True, nullable=False)

    password = db.Column(db.String(128), nullable=False)  # written as hexa
    salt = db.Column(db.String(8), nullable=False)

    disabled = db.Column(db.Boolean, nullable=False, default=False)
