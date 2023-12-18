from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity that inherits from BaseModel."""
    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance."""
        super().__init__(*args, **kwargs)
