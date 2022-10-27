from flask import request, jsonify

from models.food import FoodCategories

from utils.response import error_response
from utils.user_decorator import check_user_permission



@check_user_permission()
def show_category(place_id):
    category_id = request.args.get("id") or None
    if category_id is None:
        return error_response("bad_request")

    category = FoodCategories.get_or_none(id=category_id, place=place_id)
    if category is None:
        return error_response("category_not_found")

    category.hide = False
    category.save()

    return jsonify(), 204

#
@check_user_permission()
def hide_category(place_id):
    category_id = request.args.get("id") or None
    if category_id is None:
        return error_response("bad_request")

    category = FoodCategories.get_or_none(id=category_id, place=place_id)
    if category is None:
        return error_response("category_not_found")

    category.hide = True
    category.save()

    return jsonify(), 204

# 
@check_user_permission()
def position_category(place_id):
    item_1 = request.args.get("item_1") or None
    item_2 = request.args.get("item_2") or None

    if item_1 is None or item_2 is None:
        return error_response("bad_request")

    category_1 = FoodCategories.get_or_none(id=item_1, place=place_id)
    if category_1 is None:
        return error_response("category_not_found")

    category_2 = FoodCategories.get_or_none(id=item_2, place=place_id)
    if category_2 is None:
        return error_response("category_not_found")

    temp_category_position = category_1.position 
    category_1.position = category_2.position
    category_2.position = temp_category_position

    category_1.save()
    category_2.save()

    return jsonify(), 204

