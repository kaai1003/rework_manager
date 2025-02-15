#!/usr/bin/python3

from datetime import datetime
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
    print("Connection established")
else:
    print("Connection failed")
rework_data = {}
print("*******Start Rework********")
print("--Informations FX Rework--------------")
print("1 - Reference")
ref = input("Entez la reference FX: ")
data_ref = get_obj("reference", "ref", ref)
if data_ref is None:
    print("Reference not found")
    exit(1)
rework_data["ref"] = data_ref["ref"]
rework_data["project"] = data_ref["project"]
rework_data["famille"] = data_ref["famille"]
rework_data["car_type"] = data_ref["car_type"]
print("2 - Ligne")
line = input("Entrez la Ligne Production FX: ")
if line.isdigit():
    line = int(line)
    rework_data["line"] = line
else:
    print("Invalid line")
    exit(1)
print("3 - Superviseur")
supervisor = input("Entrez le nom du superviseur: ")
if supervisor.isalpha():
    rework_data["superviseur"] = supervisor
else:
    print("Invalid supervisor")
    exit(1)
print("4 - Production Date")
prod_date = input("Entrez la date de production (2024-02-15 14:30:00): ")
try:
    prod_date = datetime.strptime(prod_date, "%Y-%m-%d %H:%M:%S")
    rework_data["prod_date"] = prod_date
except ValueError:
    print("Invalid date format")
    exit(1)
print("--Informations Rework--------------")
print("5 - ReworkCard")
rework_card = input("Entrez le numero de la rework card: ")
if rework_card[0] == "*" and rework_card[-1] == "#":
    rework_card = rework_card[1:-1]
    if get_obj("reworkdetails", "reworkcard", rework_card):
        print("Rework card already exists")
        exit(1)
    else:
        rework_data["reworkcard"] = rework_card
else:
    print("Invalid rework card")
    exit(1)
print("6 - Erreur Type")
error_type = input("Entrez le type d'erreur: ")
rework_data["reworkfailure"] = error_type
print("7 - Erreur Description")
error_desc = input("Entrez la description de l'erreur: ")
rework_data["failuredetails"] = error_desc
print("8 - Process Rework")
process_rework = input("Entrez le process de rework: ")
rework_data["processfailure"] = process_rework
print("9 - Table de Rework")
table_rework = input("Entrez la table de rework: ")
if table_rework.isdigit():
    table_rework = int(table_rework)
    rework_data["reworktable"] = table_rework
else:
    print("Invalid table rework")
    exit(1)
print("10 - Reworker")
reworker = input("Entrez le nom du reworker: ")
rework_data["reworker"] = reworker
rework_data["status"] = "open"
print(rework_data)
rework_fx = ReworkDetails(**rework_data)
print(rework_fx)
rework_fx.save()
rework_data = {}
rework_fx = None
exit(0)