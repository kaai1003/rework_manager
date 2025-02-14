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
from models.engine.database_manager import get_obj
from models.engine.database_manager import get_all


print(get_connection())

usr1 = get_obj("users", "username", "aql1")
user1 = User(**usr1)
user1.delete()