#!/usr/bin/python3
"""Reworkers Class module"""

from models.basemodel import BaseModel

class Reworkers(BaseModel):
    def __init__(self, *args, **kwargs):
        """Object init"""
        super().__init__(*args, **kwargs)
