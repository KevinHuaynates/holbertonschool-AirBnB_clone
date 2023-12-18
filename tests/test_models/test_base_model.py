#!/usr/bin/python3
from models.base_model import BaseModel
import time

# Test BaseModel: instance creation
my_model = BaseModel()

# Test BaseModel: id type
assert type(my_model.id) == str, "Incorrect output : Test BaseModel: self.id"

# Test BaseModel: created_at type
assert type(my_model.created_at) == datetime, "Incorrect output : Test BaseModel: self.created_at"

# Test BaseModel: 2 instances creation with different id
my_model_2 = BaseModel()
assert my_model.id != my_model_2.id, "Incorrect output : Test BaseModel: 2 instances creation + id different"

# Test BaseModel: __str__ implementation
output_str = str(my_model)
expected_output_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
assert output_str.strip() == expected_output_str.strip(), "Incorrect output : Test BaseModel: __str__(self)"

# Test BaseModel: to_dict() type
my_model_dict = my_model.to_dict()
assert type(my_model_dict) == dict, "Incorrect output : Test BaseModel: to_dict()"

# Test BaseModel: save() and updated_at type
original_updated_at = my_model.updated_at
my_model.save()
assert my_model.updated_at > original_updated_at, "Incorrect output : Test BaseModel: save()"
