#!/usr/bin/env python3
import os

SQLALCHEMY_DB_URI = ""
JWT_PRIVATE_KEY = ""
JWT_PUBLIC_KEY = ""

# and now, let's override this

SQLALCHEMY_DB_URI = os.environ.get("TOKENSERIVCE_DB_URI",SQLALCHEMY_DB_URI)

if "TOKENSERVICE_PRIVATE_KEY" in os.environ:
	JWT_PRIVATE_KEY = open(os.environ["TOKENSERVICE_PRIVATE_KEY"],'r').read()

if "TOKENSERVICE_PUBLIC_KEY" in os.environ:
	JWT_PUBLIC_KEY = open(os.environ["TOKENSERVICE_PUBLIC_KEY"],'r').read()
