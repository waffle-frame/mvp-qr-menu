from datetime import timedelta
from json import loads as jloads

from flask import request
from flask import Blueprint, render_template, abort, jsonify
from flask_jwt_extended import create_access_token

from models.users import Users
from models.places import Places

from utils.response import error_response

admin_auth = Blueprint(
    "admin_auth", 
    __name__,
    url_prefix='/admin'
)


@admin_auth.route("/<place>/auth", methods=["POST"])
def auth(place):
    # Сheck for the existence of the place
    place = Places.get_or_none(name=place)
    if place is None:
        return error_response("place_not_found")

    # Try get form-data from request
    text_json = request.get_data()
    try:
        form = jloads(text_json)
        username = form["username"]
        password = form["password"]
    except Exception as e:
        return error_response("bad_request")

    # Check user data
    userdata = Users.get_or_none(username=username, password=password)
    if userdata is None:
        return error_response("wrong_data")

    if userdata.id != place.user.id:
        return error_response("permission_denied")

    # Generate access token
    access_token = {
        "access_token": create_access_token(
            identity=userdata.id, 
            expires_delta=timedelta(days=30)
        ),
    }

    return jsonify(access_token) 
