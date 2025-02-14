#!/usr/bin/python3
"""Rework Details Class module"""

from models.basemodel import BaseModel

class ReworkDetails(BaseModel):
    def __init__(self, *args, **kwargs):
        """Object init"""
        super().__init__(*args, **kwargs)
