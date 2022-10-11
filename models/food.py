from peewee import *

from models.places import Places
from models.base import BaseModel

# Категории еды
class FoodCategories(BaseModel):
    name = CharField()
    hide = BooleanField(default=False)
    position = IntegerField()
    place = ForeignKeyField(Places)

# Еда
class Food(BaseModel):
    photo = CharField()
    name = CharField()
    composition = TextField()
    time_for_preparing = FloatField()
    weight = IntegerField()
    price = FloatField()
    hide = BooleanField(default=False)
    position = IntegerField()

# Промежуточная таблица
class RelationshipFoodCategories(BaseModel):
    food = ForeignKeyField(Food)
    category = ForeignKeyField(FoodCategories)
