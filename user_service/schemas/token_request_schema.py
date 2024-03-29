#!/usr/bin/env python3
from marshmallow import Schema, fields
import marshmallow.validate

#
# This schema is not bound to any data model, since this is only used for login requests
#


class TokenRequestSchema(Schema):
	name = fields.String(load_only=True, required=True, allow_none=False, validate=[marshmallow.validate.Length(max=128), marshmallow.validate.Regexp("[a-zA-Z0-9_]*")])
	password = fields.String(load_only=True, required=True, allow_none=False)

	class Meta:
		pass
