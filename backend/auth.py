from db import get_connection
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
import bcrypt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():

    print("Reqquest header:", request.headers)
    print("Request data:", request.data)
    print("Request json:", request.json)

    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"error": "username and password ไม่มีค่า"}, 400
    
    try:
        conn = get_connection()
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT user_id, password FROM users WHERE user_name = %s",
                    (username,),
                )
                user = cursor.fetchone()
        
        if user is None:
            return {"error": "not found user"}, 404
        
        user_id, user_name, hashed_passord = user

        if bcrypt.checkpw(password.encode("utf-8"), hashed_passord.encode("utf-8")):
            access_token = create_access_token(
                identity = user_name,
                additional_claims = {"user_id": user_id}
            )

            return jsonify({"access_token": access_token}), 200
        else:
            return {"erroe": "invalid password"}, 401

    except Exception as e:
        return {"error": str(e)}, 500