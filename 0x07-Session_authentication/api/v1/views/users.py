#!/usr/bin/env python3
""" Módulo de Vistas de Usuarios
"""
from api.v1.views import app_vista
from flask import abort, jsonify, request
from models.user import User


@app_vista.route('/users', methods=['GET'], strict_slashes=False)
def view_all_users() -> str:
    """ OBTENER /api/v1/usuarios
    Regreso:
      - lista de todos los objetos de usuario representados por JSON
    """
    all_users = [user.to_json() for user in User.all()]
    return jsonify(all_users)


@app_vista.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def view_one_user(user_id: str = None) -> str:
    """ OBTENER /api/v1/usuarios/:id
    Parámetro de ruta:
      - Identificación de usuario
    Regreso:
      - Objeto de usuario JSON representado
      - 404 si el ID de usuario no existe
    """
    if user_id == "me" and request.current_user is None:
        abort(404)
    if user_id == "me" and request.current_user is not None:
        return jsonify(request.current_user.to_json())
    if user_id is None:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())


@app_vista.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id: str = None) -> str:
    """ ELIMINAR /api/v1/usuarios/:id
    Parámetro de ruta:
      - Identificación de usuario
    Regreso:
      - JSON vacío es que el usuario se eliminó correctamente
      - 404 si el ID de usuario no existe
    """
    if user_id is None:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.remove()
    return jsonify({}), 200


@app_vista.route('/users', methods=['POST'], strict_slashes=False)
def create_user() -> str:
    """ POST /api/v1/usuarios/
    Cuerpo JSON:
      - Email
      - clave
      - apellido (opcional)
      - Nombre (opcional)
    Regreso:
      - Objeto de usuario JSON representado
      - 400 si no se puede crear el nuevo Usuario
    """
    rj = None
    error_msg = None
    try:
        rj = request.get_json()
    except Exception as e:
        rj = None
    if rj is None:
        error_msg = "Wrong format"
    if error_msg is None and rj.get("email", "") == "":
        error_msg = "email missing"
    if error_msg is None and rj.get("password", "") == "":
        error_msg = "password missing"
    if error_msg is None:
        try:
            user = User()
            user.email = rj.get("email")
            user.password = rj.get("password")
            user.first_name = rj.get("first_name")
            user.last_name = rj.get("last_name")
            user.save()
            return jsonify(user.to_json()), 201
        except Exception as e:
            error_msg = "Can't create User: {}".format(e)
    return jsonify({'error': error_msg}), 400


@app_vista.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id: str = None) -> str:
    """ PUT /api/v1/usuarios/:id
    Parámetro de ruta:
      - Identificación de usuario
    Cuerpo JSON:
      - apellido (opcional)
      - Nombre (opcional)
    Regreso:
      - Objeto de usuario JSON representado
      - 404 si el ID de usuario no existe
      - 400 si no se puede actualizar el Usuario
    """
    if user_id is None:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    rj = None
    try:
        rj = request.get_json()
    except Exception as e:
        rj = None
    if rj is None:
        return jsonify({'error': "Wrong format"}), 400
    if rj.get('first_name') is not None:
        user.first_name = rj.get('first_name')
    if rj.get('last_name') is not None:
        user.last_name = rj.get('last_name')
    user.save()
    return jsonify(user.to_json()), 200
