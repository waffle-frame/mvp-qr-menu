from flask import request, jsonify, send_file

from models.banners import Banners

from utils.response import error_response
from utils.user_decorator import check_user_permission
from settings.configurations import NO_PHOTO_FILENAME, MEDIA_DIR



@check_user_permission()
def get_banner_list(place_id):
    banners_list = Banners.select().where(
        Banners.place==place_id,
        Banners.hide==False
    )

    data = {}

    for i in banners_list:
        data[i.id] = i.name

    return jsonify(data)


# 
@check_user_permission()
def get_banner_photo(place_id):
    banner_id = request.args.get("id") or None
    if banner_id is None:
        return error_response("bad_request")

    banner = Banners.get_or_none(id=banner_id, place=place_id)
    if banner is None:
        return error_response("banner_not_found")

    try:
        return send_file(MEDIA_DIR + banner.photo)
    except FileNotFoundError:
        return send_file(MEDIA_DIR + NO_PHOTO_FILENAME)
    else:
        return error_response("internal_server")