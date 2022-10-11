from os import remove
from random import randint
from flask import request, jsonify

from models.banners import Banners

from utils.create_file import MEDIA_DIR
from utils.response import error_response
from utils.user_decorator import check_user_permission


@check_user_permission()
def update_banner(place_id, place):
    # Try get banner name and banner photo as file
    try:
        banner_id = request.form["id"]
        banner_name = request.form["name"]
        banner_photo = request.files["photo"]
    except Exception as e:
        return error_response("bad_request")

    banner = Banners.get_or_none(id=banner_id, place=place_id)
    if banner is None:
        return error_response("banner_not_found")

    try:
        remove(MEDIA_DIR + banner.photo)
    except FileNotFoundError:
        pass
    except Exception as e:
        return error_response("internal_server")

    # Create new name and save file
    banner_photo_path = f"{place}/banners/{randint(10000, 99999)}_{banner_photo.filename}"
    banner_photo.save(MEDIA_DIR + banner_photo_path)
    
    
    # Update data
    banner.name = banner_name
    banner.photo = banner_photo_path
    banner.save()

    return jsonify(), 204
