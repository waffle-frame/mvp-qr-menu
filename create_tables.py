import sqlite3

from peewee import *

from models.base import sqlite

from models.users import Users
from models.places import Places
from models.banners import Banners
from models.food import Food, FoodCategories, RelationshipFoodCategories


def create_tables():
    with sqlite:
        sqlite.create_tables([Users, Places, Banners, Food, FoodCategories, RelationshipFoodCategories])

create_tables()