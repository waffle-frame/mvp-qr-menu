from flask import Flask

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from apps.admin.auth.auth import admin_auth
from apps.admin.banners.blueprint import admin_banner
# from apps.admin.banners.update import update_banner
from settings.configurations import SECRET_KEY, JWT_SECRET_KEY



app = Flask(__name__)
jwt = JWTManager(app)

app.config["SECRET_KEY"] = SECRET_KEY
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY



app.register_blueprint(admin_auth)
app.register_blueprint(admin_banner)


@app.route('/')
@jwt_required()
def index():
    return "index"

if __name__ == "__main__":
    app.run(debug=True)
