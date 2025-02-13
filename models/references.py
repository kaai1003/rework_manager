#!/usr/bin/python3
"""Harness Class module"""

from models.basemodel import BaseModel

class Reference(BaseModel):
    def __init__(self, *args, **kwargs):
        """Object init"""
        super().__init__(*args, **kwargs)
