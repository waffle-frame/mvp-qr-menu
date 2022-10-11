from flask import Flask

from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import create_access_token

from apps.admin.auth.auth import admin_auth
from apps.admin.banners.blueprint import admin_banner
from apps.admin.food_categories.blueprint import admin_food_categories

from settings.configurations import SECRET_KEY, JWT_SECRET_KEY


app = Flask(__name__)
jwt = JWTManager(app)

app.config["SECRET_KEY"] = SECRET_KEY
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY

app.register_blueprint(admin_auth)
app.register_blueprint(admin_banner)
app.register_blueprint(admin_food_categories)


if __name__ == "__main__":
    app.run(debug=True)
