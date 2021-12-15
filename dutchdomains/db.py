import os

from peewee import SqliteDatabase
from peewee import Model, CharField, AutoField, ForeignKeyField, FloatField

DB_LOCATION = os.environ.get('DB_LOCATION', ':memory:')

if DB_LOCATION != ":memory:" and not os.path.exists(DB_LOCATION):
    raise Exception(f"Database file {DB_LOCATION} not found!")

print(f"Using database at {DB_LOCATION}")
db = SqliteDatabase(DB_LOCATION, pragmas={'foreign_keys': 1})

class Category(Model):
    id = AutoField()
    klazify_label = CharField(max_length=255)
    label = CharField(max_length=255, null=True)

    class Meta:
        database = db


class SubCategory(Model):
    id = AutoField()
    category = ForeignKeyField(Category)
    klazify_label = CharField(max_length=255)

    class Meta:
        database = db


class Domain(Model):
    id = AutoField()
    url = CharField(max_length=255)
    logo = CharField(max_length=255, null=True)
    main_category = ForeignKeyField(Category, null=True)

    class Meta:
        database = db


class Categorization(Model):
    id = AutoField()
    domain = ForeignKeyField(Domain)
    subcategory = ForeignKeyField(SubCategory)
    confidence = FloatField()

    class Meta:
        database = db


def initialize_if_needed():
    db.create_tables([Category, SubCategory, Domain, Categorization])
