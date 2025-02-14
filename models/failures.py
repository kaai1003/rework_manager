#!/usr/bin/python3
"""Failures Class module"""

from models.basemodel import BaseModel

class Failure(BaseModel):
    def __init__(self, *args, **kwargs):
        """Object init"""
        super().__init__(*args, **kwargs)
