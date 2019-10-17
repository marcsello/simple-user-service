#!/usr/bin/env python3
from .db import db
from sqlalchemy.sql import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)

    name = db.Column(db.String(128), unique=True, nullable=False)

    password = db.Column(db.String(128), nullable=False)  # written as hexa
    salt = db.Column(db.String(8), nullable=False)

    created = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())

    disabled = db.Column(db.Boolean, nullable=False, default=False)
