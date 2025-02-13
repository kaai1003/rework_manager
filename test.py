#!/usr/bin/python3

from models.references import Reference


ref1_dict = {"ref": "123456 01",
             "project": "P21",
             "famille": "PPL",
             "car_type": "Thermique"}
ref1 = Reference(**ref1_dict)
print(ref1.__dict__)
ref2 = Reference()
print(ref2.__dict__)
ref2.ref = "123432 02"
print(ref2.to_dict())