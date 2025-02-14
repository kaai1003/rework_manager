#!/usr/bin/python3
"""Rework Tables Class module"""

from models.basemodel import BaseModel

class ReworkTable(BaseModel):
    def __init__(self, *args, **kwargs):
        """Object init"""
        super().__init__(*args, **kwargs)
