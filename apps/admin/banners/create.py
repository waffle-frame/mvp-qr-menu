from random import randint
from flask import request, jsonify

from models.banners import Banners

from utils.response import error_response
from utils.user_decorator import check_user_permission
from utils.create_file import create_folders, MEDIA_DIR



@check_user_permission()
def create_banner(place_id, place):
    # Try get banner name and banner photo as file
    try:
        banner_name = request.form["name"]
        banner_photo = request.files["photo"]
    except Exception as e:
        return error_response("bad_request")

    # Set file locate
    banner_photo_path = f"{place}/banners/{randint(10000, 99999)}_{banner_photo.filename}"

    try:
        banner_photo.save(MEDIA_DIR + banner_photo_path)
    except FileNotFoundError as e:
        create_folders(place)
        banner_photo.save(MEDIA_DIR + banner_photo_path)
    except Exception as e:
        print(e)
        return error_response("internal_server")

    Banners(
        photo = banner_photo_path,
        name = banner_name,
        position = Banners.select().where(Banners.place==place_id).count() + 1,
        place = place_id
    ).save()

    return jsonify(), 201
