#!/usr/bin/env python3
"""
modulo de la api
"""
from os import getenv
from api.v1.views import app_vista
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_vista)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auto = None

if getenv("AUTH_TYPE") == "auth":
    from api.v1.auth.auth import Auth
    auto = Auth()

if getenv("AUTH_TYPE") == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auto = BasicAuth()

if getenv("AUTH_TYPE") == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auto = SessionAuth()

if getenv("AUTH_TYPE") == "session_exp_auth":
    from api.v1.auth.session_exp_auth import SessionExpAuth
    auto = SessionExpAuth()


@app.before_request
def before_request_func():
    """crear una función antes de la solicitud para comprobar si el usuario ha iniciado sesión
    """
    if auto is not None:
        endpoints = ['/api/v1/status/',
                     '/api/v1/unauthorized/', '/api/v1/forbidden/',
                     '/api/v1/auth_session/login/']
        if auto.require_auth(request.path, endpoints) is True:

            if ((auto.authorization_header(request) is None)
                    and (auto.session_cookie(request) is None)):
                abort(401)
            user = auto.current_user(request)
            if user is None:
                abort(403)
            request.current_user = user


@ app.errorhandler(404)
def not_found(error) -> str:
    """ Controladora no encontrada
    """
    return jsonify({"error": "Not found"}), 404


@ app.errorhandler(401)
def unauthorized(error) -> str:
    """ controlador de solicitudes no autorizado
    """
    return jsonify({"error": "Unauthorized"}), 401


@ app.errorhandler(403)
def forbidden(error) -> str:
    """Controlador de solicitudes prohibidas
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
