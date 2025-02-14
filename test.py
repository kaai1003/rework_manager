#!/usr/bin/python3

from models.references import Reference
from models.failures import Failure
from models.lines import Line
from models.process import Process
from models.projects import Project
from models.reworkdetails import ReworkDetails
from models.reworkers import Reworkers
from models.reworktables import ReworkTable
from models.users import User
from models.engine.database_manager import get_connection


print(get_connection())


ref1_dict = {"ref": "123456 01",
             "project": "P21",
             "famille": "PPL",
             "car_type": "Thermique"}
ref1 = Reference(**ref1_dict)
print("-------Reference1--------")
print(ref1.__dict__)
ref2 = Reference()
print("-------Reference2--------")
print(ref2.__dict__)
ref2.ref = "123432 02"
print("-------Reference1:ref--------")
print(ref2.to_dict())