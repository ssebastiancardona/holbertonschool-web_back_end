#!/usr/bin/env python3
""" humm
"""
from flask import Blueprint

app_vista = Blueprint("app_vista", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *

User.load_from_file()
