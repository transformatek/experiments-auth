# -*- coding: utf-8 -*-
# Part of Odyte platform
# Copyright (c) INFINITGRAPH INTELLIGENCE LLC, TAMPA, FL 33602, USA

from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app.models.product import Product

from app import appbuilder, db


class ProductModelView(ModelView):
    datamodel = SQLAInterface(Product)
    list_columns = ["id", "name"]
    base_order = ("id", "desc")


db.create_all()
appbuilder.add_view(
    ProductModelView,
    "Product",
    icon="fa fa-binoculars",
    category_icon="fa fa-binoculars",
    category="Product",
)