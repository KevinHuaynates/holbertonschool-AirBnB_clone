import uuid
from datetime import datetime


class BaseModel:
    """Base model for AirBnB project."""
    def __init__(self, *args, **kwargs):
        """Initialize base model instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Return string of BaseModel."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ """
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict
