from flask import Blueprint

from apps.admin.banners.create import create_banner
from apps.admin.banners.update import update_banner
from apps.admin.banners.get import get_banner_list, get_banner_photo
from apps.admin.banners.state import show_banner, hide_banner, position_banner

admin_banner = Blueprint(
    "admin_banner",
    __name__,
    url_prefix="/admin",
)


admin_banner.add_url_rule(
    "/<place>/banners/create", 'admin_banners_create',
    view_func=create_banner, methods=["POST"]
)

admin_banner.add_url_rule(
    "/<place>/banners/update", 'admin_banners_update',
    view_func=update_banner, methods=["POST"]
)

admin_banner.add_url_rule(
    "/<place>/banners/get_list", 'admin_get_banner_list',
    view_func=get_banner_list, methods=["GET"]
)

admin_banner.add_url_rule(
    "/<place>/banners/get_photo", 'admin_get_banner_photo',
    view_func=get_banner_photo, methods=["GET"]
)

admin_banner.add_url_rule(
    "/<place>/banners/show", 'admin_show_banner',
    view_func=show_banner, methods=["GET"]
)

admin_banner.add_url_rule(
    "/<place>/banners/hide", 'admin_hide_banner',
    view_func=hide_banner, methods=["GET"]
)

admin_banner.add_url_rule(
    "/<place>/banners/position", 'admin_position_banner',
    view_func=position_banner, methods=["GET"]
)
