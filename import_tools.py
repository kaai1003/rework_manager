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
from models.engine.database_manager import load_csv

if get_connection():
    print("Connection Established")
else:
    print("Connection Failed")
    exit(1)

print("--------Welcome to Tool Importer--------")
print("Select table to Import:\n1- Users\n2- failures\n3- lines\n4- process\n5- projects\n6- references\n7- reworkers\n8- reworktables")

table_selected = input("please type number of table to be Imported: ")

if table_selected == "1":
    users = load_csv("users.csv")
    for user in users:
        obj = User(**user)
        obj.save()
    exit(0)
elif table_selected == "2":
    failures = load_csv("failures.csv")
    for f in failures:
        obj = Failure(**f)
        obj.save()
    exit(0)
elif table_selected == "3":
    lines = load_csv("lines.csv")
    for l in lines:
        obj = Line(**l)
        obj.save()
    exit(0)
elif table_selected == "4":
    process = load_csv("lines.csv")
    for p in process:
        obj = Process(**p)
        obj.save()
        exit(0)
elif table_selected == "5":
    projects = load_csv("projects.csv")
    for p in projects:
        obj = Project(**p)
        obj.save()
    exit(0)
elif table_selected == "6":
    refs = load_csv("refs.csv")
    for ref in refs:
        obj = Reference(**ref)
        obj.save()
    exit(0)
elif table_selected == "7":
    reworkers = load_csv("reworkers.csv")
    for r in reworkers:
        obj = Reworkers(**r)
        obj.save()
    exit(0)
elif table_selected == "8":
    tables = load_csv("reworkers.csv")
    for r in tables:
        obj = ReworkTable(**r)
        obj.save()
    exit(0)
else:
    print("incorrect Selection, please try again")
    exit(1)
#list_users = []
#users = get_all("users")
#for user in users:
#    list_users.append(user["username"])
#print(list_users)

refs = load_csv("refs.csv")
for ref in refs:
    obj = Reference(**ref)
    obj.save()