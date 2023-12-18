#!/usr/bin/python3
"""
BaseModel module
"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Initialization method"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

    def to_dict(self):
        """Returns a dictionary"""
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result

    def __str__(self):
        """Returns the string representation of the instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )


if __name__ == "__main__":
    bm1 = BaseModel()
    bm2 = BaseModel(**bm1.to_dict())
    print(bm1 is not bm2)
