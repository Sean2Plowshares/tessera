from tessera import cache, app
from tessera.v1.models import User
from tessera.lib.tokens import create_token, auth_required, admin_required
from flask import jsonify, request, g
from tessera.v1 import v1

@v1.route("/users", methods=["GET"])
@admin_required
def user_index():
    users = [ u.to_json() for u in User.query.all() ]
    return jsonify(users)

@v1.route("/users", methods=["POST"])
def user_create():
    ujson = request.get_json()
    u = User.from_json(ujson)
    u.save()
    return jsonify(message="User succesfully created.")

@v1.route("/users/<username>", methods=["GET"])
@auth_required
def user_get(username):
    u = User.get_by_username_or_id(username)
    return jsonify(u.to_json())

@v1.route("/users/<username>", methods=["PUT"])
@auth_required
def user_update(username):
    if g.user.id == u.id or not g.user.is_admin:
        ujson = request.get_json()
        u = User.query.filter_by(username=username).first() 
        u.update(u)
        save_model(u, "That username is already taken.")
        return jsonify(message="User successfully updated.")

    raise AppError(message="Access denied.", status_code = 403)
    
