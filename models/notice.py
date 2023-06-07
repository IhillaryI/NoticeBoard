#!/usr/bin/python3

import models
from models.base import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Notice(BaseModel, Base):
    __tablename__ = "notices"
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    title = Column(String(60), nullable=False)
    text = Column(String(1024), nullable=False)
