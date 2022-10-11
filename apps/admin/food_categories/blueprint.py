from flask import Blueprint

from apps.admin.food_categories.create import create_category
from apps.admin.food_categories.update import update_category
from apps.admin.food_categories.get import get_categories_list
from apps.admin.food_categories.state import show_category, hide_category, position_category

admin_food_categories = Blueprint(
    "admin_food_categories",
    __name__,
    url_prefix="/admin",
)


admin_food_categories.add_url_rule(
    "/<place>/categories/create", 'admin_categories_create',
    view_func=create_category, methods=["POST"]
)

admin_food_categories.add_url_rule(
    "/<place>/categories/update", 'admin_categories_update',
    view_func=update_category, methods=["POST"]
)

admin_food_categories.add_url_rule(
    "/<place>/categories/get_list", 'admin_categories_list',
    view_func=get_categories_list, methods=["GET"]
)

admin_food_categories.add_url_rule(
    "/<place>/categories/show", 'admin_categories_show',
    view_func=show_category, methods=["GET"]
)

admin_food_categories.add_url_rule(
    "/<place>/categories/hide", 'admin_categories_hide',
    view_func=hide_category, methods=["GET"]
)

admin_food_categories.add_url_rule(
    "/<place>/categories/position", 'admin_categories_position',
    view_func=position_category, methods=["GET"]
)
