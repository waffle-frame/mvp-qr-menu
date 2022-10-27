from random import randint
from flask import request, jsonify

from models.food import Food, FoodCategories

from settings.configurations import NO_PHOTO_FILENAME
from utils.response import error_response
from utils.user_decorator import check_user_permission
from utils.create_file import create_folders, MEDIA_DIR



@check_user_permission()
def create_food(place_id):
    # Try get food data and food photo as file
    try:
        food_name = request.form["name"]
        food_price = request.form["price"]
        food_photo = request.files["photo"]
        food_weight = request.form["weight"]
        food_compound = request.form["compound"]
        food_time_for_preparing = request.form["time_for_preparing"]
    except Exception as e:
        return error_response("bad_request")

    # Set photo locate
    if food_photo.content_length != 0:
        food_photo_path = f"{place.name}/food/{randint(10000, 99999)}_{banner_photo.filename}"
    else:
        food_photo_path = NO_PHOTO_FILENAME

    try:
        food_photo.save(MEDIA_DIR + food_photo_path)
    except FileNotFoundError as e:
        create_folders(place)
        food_photo.save(MEDIA_DIR + food_photo_path)
    except Exception as e:
        print(e)
        return error_response("internal_server")

    Food(
        photo = food_photo_path,
        name = food_photo,
        composition = food_compound,
        time_for_preparing = food_time_for_preparing,
        weight = food_weight,
        price = food_price,
        position = Food.select().where(Food.place==place_id).count() + 1,
    )

    return jsonify(), 201
