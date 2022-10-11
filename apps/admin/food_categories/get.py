from flask import request, jsonify

from models.food import FoodCategories

from utils.response import error_response
from utils.user_decorator import check_user_permission



@check_user_permission()
def get_categories_list(place_id, place):
    categories_list = FoodCategories.select().where(
        FoodCategories.place==place_id,
        FoodCategories.hide==False
    )

    data = {}

    for i in categories_list:
        data[i.id] = i.name

    return jsonify(data)
