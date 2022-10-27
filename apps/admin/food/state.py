from flask import request, jsonify

from models.banners import Banners

from utils.create_file import MEDIA_DIR
from utils.response import error_response
from utils.user_decorator import check_user_permission



@check_user_permission()
def show_banner(place_id, place):
    banner_id = request.args.get("id") or None
    if banner_id is None:
        return error_response("bad_request")

    banner = Banners.get_or_none(id=banner_id, place=place_id)
    if banner is None:
        return error_response("banner_not_found")

    banner.hide = False
    banner.save()

    return jsonify(), 204

#
@check_user_permission()
def hide_banner(place_id, place):
    banner_id = request.args.get("id") or None
    if banner_id is None:
        return error_response("bad_request")

    banner = Banners.get_or_none(id=banner_id, place=place_id)
    if banner is None:
        return error_response("banner_not_found")

    banner.hide = True
    banner.save()

    return jsonify(), 204

# 
@check_user_permission()
def position_banner(place_id, place):
    item_1 = request.args.get("item_1") or None
    item_2 = request.args.get("item_2") or None

    if item_1 is None or item_2 is None:
        return error_response("bad_request")

    banner_1 = Banners.get_or_none(id=item_1, place=place_id)
    if banner_1 is None:
        return error_response("banner_not_found")

    banner_2 = Banners.get_or_none(id=item_2, place=place_id)
    if banner_2 is None:
        return error_response("banner_not_found")

    temp_banner_position = banner_1.position 
    banner_1.position = banner_2.position
    banner_2.position = temp_banner_position

    banner_1.save()
    banner_2.save()

    return jsonify(), 204

