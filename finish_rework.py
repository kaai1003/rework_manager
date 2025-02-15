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

print("*******Finish Rework********")
print("--Informations FX Rework--------------")
rework_card = input("Entrez le numero de la rework card: ")
rework_data = get_obj("reworkdetails", "reworkcard", rework_card)
if rework_data is None:
    print("FX not found")
    exit(1)
elif rework_data["status"] == "Finished":
    print("FX already finished")
    exit(1)
print("REF: {}\n\
Project: {}\n\
Famille: {}\n\
Car Type: {}\n\
Line: {}\n\
Supervisor: {}\n\
Production Date: {}\n\
Erreur: {}\n\
Erreur Details: {}".format(rework_data["ref"],
                           rework_data["project"],
                           rework_data["famille"],
                           rework_data["car_type"],
                           rework_data["line"],
                           rework_data["superviseur"],
                           rework_data["prod_date"],
                           rework_data["reworkfailure"],
                           rework_data["failuredetails"]))
rework_fx = ReworkDetails(**rework_data)
print("------Quality Control------")
aql = input("AQL: ")
rework_fx.quality = aql
rework_fx.status = "Finished"
rework_time = datetime.now() - rework_fx.created_at
rework_time = rework_time.total_seconds() / 60
rework_fx.reworkduration = round(rework_time, 2)
rework_fx.update()

exit(0)