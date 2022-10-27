from json import loads as jloads
from flask import request, jsonify

from models.food import FoodCategories

from utils.response import error_response
from utils.user_decorator import check_user_permission


@check_user_permission()
def create_category(place_id):
    text_json = request.get_data()
    try:
        form = jloads(text_json)
        category_name = form["name"]
    except Exception as e:
        return error_response("bad_request")

    FoodCategories(
        name = category_name,
        place = place_id,
        position = FoodCategories.select().where(FoodCategories.place==place_id).count() + 1,
    ).save()

    return jsonify(), 201
