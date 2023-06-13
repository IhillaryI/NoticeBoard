#!/usr/bin/python3

import models
from models.base import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from hashlib import md5
import hashlib

class User(BaseModel, Base):
    __tablename__ = 'users'
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    notices = relationship("Notice", backref="user")

    def __init__(self, *args, **kwargs):
        md5 = hashlib.md5()
        password = kwargs.get('password')
        md5.update(password.encode('utf-8'))
        kwargs['password'] = md5.hexdigest()
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        if name == "password":
            pass
            #value = md5(value.encode('utf-8')).hexdigest()
        super().__setattr__(name, value)
