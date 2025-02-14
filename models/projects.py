#!/usr/bin/python3
"""Projects Class module"""

from models.basemodel import BaseModel

class Project(BaseModel):
    def __init__(self, *args, **kwargs):
        """Object init"""
        super().__init__(*args, **kwargs)
