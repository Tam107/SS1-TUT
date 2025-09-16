from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from ..services.auth_service import register_user
from ..models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    user = register_user(data["username"], data["password"])
    if not user:
        return jsonify({"message": "User already exists"}), 400
    return jsonify({"message": "Registered successfully"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.check_password(data["password"]):
        token = create_access_token(identity=user.id)
        return jsonify({"access_token": token})
    return jsonify({"message": "Invalid credentials"}), 401
