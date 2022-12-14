from random import randint
from flask import request, jsonify

from models.places import Places
from models.banners import Banners

from utils.response import error_response
from utils.create_file import create_folders
from utils.user_decorator import check_user_permission
from settings.configurations import MEDIA_DIR, NO_PHOTO_FILENAME 


@check_user_permission()
def create_banner(place_id):
    # Try get banner name and banner photo as file
    try:
        banner_name = request.form["name"]
        banner_photo = request.files["photo"]
    except Exception as e:
        return error_response("bad_request")

    # Get place name
    place = Places.get_or_none(id=place_id)
    if place is None:
        return error_response("permission_denied")

    print(dir(banner_photo.headers), banner_photo.headers)

    # Set photo locate
    if banner_photo.filename != "":
        banner_photo_path = f"{place.name}/banners/{randint(10000, 99999)}_{banner_photo.filename}"
    else:
        banner_photo_path = NO_PHOTO_FILENAME

    try:
        banner_photo.save(MEDIA_DIR + banner_photo_path)
    except FileNotFoundError as e:
        create_folders(place.name)
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
