#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.save()

output_after_save = str(my_model)
expected_output_after_save = "[BaseModel] ({}) {}".format(my_model.id,
                                                          my_model.__dict__)
assert output_after_save == expected_output_after_save,
"Incorrect output : Test BaseModel: save()"
