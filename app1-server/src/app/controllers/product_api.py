# -*- coding: utf-8 -*-
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.api import ModelRestApi
from app import appbuilder
from app.models.product import Product
from app import appbuilder



class ProductModelApi(ModelRestApi):
    resource_name = "product"
    base_order = ("id", "desc")
    datamodel = SQLAInterface(Product)


appbuilder.add_api(ProductModelApi)