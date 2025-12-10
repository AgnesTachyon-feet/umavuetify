from db import get_connection
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
import bcrypt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return ("error": "username and password ไม่มีค่า"), 400
    
    try:
        

    except Exception as e:
        return {"error": str(e)}, 500