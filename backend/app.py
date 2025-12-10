from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import JWT_SECRET_KEY
from auth import auth_bp

app = Flask(__name__)

CORS(app)

app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY

jwt = JWTManager(app)
app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

@app.route("/")
def root():
    return {"Hello": "Uma"}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)