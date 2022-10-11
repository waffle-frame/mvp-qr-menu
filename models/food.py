from peewee import *

from models.base import BaseModel
from models.places import Places

# Категории еды
class FoodCategories(BaseModel):
    name = CharField()
    place = ForeignKeyField(Places)

# Еда
class Food(BaseModel):
    photo = CharField()
    name = CharField()
    composition = TextField()
    time_for_preparing = FloatField()
    weight = IntegerField()
    price = FloatField()
    hide = BooleanField()
    position = IntegerField()

# Промежуточная таблица
class RelationshipFoodCategories(BaseModel):
    food = ForeignKeyField(Food)
    category = ForeignKeyField(FoodCategories)
