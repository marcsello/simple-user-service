#!/usr/bin/env python3
from marshmallow import Schema, fields
import marshmallow.validate


class TokenRequestSchema(Schema):
	username = fields.String(load_only=True, required=True, allow_none=False, validate=[marshmallow.validate.Length(max=128), marshmallow.validate.Regexp("[a-zA-Z0-9_]*")])
	password = fields.String(load_only=True, required=True, allow_none=False)

	class Meta:
		pass
