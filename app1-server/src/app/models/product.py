# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from flask_appbuilder import Model


class Product(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return self.name