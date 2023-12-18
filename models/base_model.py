import uuid
from datetime import datetime


class BaseModel:
    """Base model for AirBnB project."""
    def __init__(self, *args, **kwargs):
        """Initialize a new instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        data = self.__dict__.copy()
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
