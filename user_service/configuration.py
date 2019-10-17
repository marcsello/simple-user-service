#!/usr/bin/env python3
import os

SQLALCHEMY_DB_URI = ""
JWT_PRIVATE_KEY = ""
JWT_PUBLIC_KEY = ""

# and now, let's override this

SQLALCHEMY_DB_URI = os.environ.get("USERSERIVCE_DB_URI",SQLALCHEMY_DB_URI)

if "USERSERVICE_PRIVATE_KEY" in os.environ:
	JWT_PRIVATE_KEY = open(os.environ["USERSERVICE_PRIVATE_KEY"],'r').read()

if "USERSERVICE_PUBLIC_KEY" in os.environ:
	JWT_PUBLIC_KEY = open(os.environ["USERSERVICE_PUBLIC_KEY"],'r').read()
