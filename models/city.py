from models.base_model import BaseModel

class City(BaseModel):
    """Class City that inherits from BaseModel."""
    def __init__(self, *args, **kwargs):
        """Initialize City instance."""
        super().__init__(*args, **kwargs)
        # Add any specific attributes for City here

