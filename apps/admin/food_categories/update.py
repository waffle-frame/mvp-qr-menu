from json import loads as jloads
from flask import request, jsonify

from models.food import FoodCategories

from utils.response import error_response
from utils.user_decorator import check_user_permission


@check_user_permission()
def update_category(place_id, place):
    text_json = request.get_data()
    try:
        form = jloads(text_json)
        category_id = form["id"]
        category_name = form["name"]
    except Exception as e:
        return error_response("bad_request")

    category = FoodCategories.get_or_none(category_id)
    if category is None:
        return error_response("food_category_not_found")

    category.name = category_name
    category.save()

    return jsonify(), 204
