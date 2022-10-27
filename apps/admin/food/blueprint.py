from flask import Blueprint

from apps.admin.food.create import create_food

admin_food = Blueprint(
    "admin_food",
    __name__,
    url_prefix= "/admin",
)


admin_food.add_url_rule(
    "/<place>/caregories/<category_id>/food/create", 'admin_create_food_in_category',
    view_func=create_food, methods=["POST"]
)
    