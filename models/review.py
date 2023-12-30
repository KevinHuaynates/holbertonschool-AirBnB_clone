from models.base_model import BaseModel

class Review(BaseModel):
    """Class Review that inherits from BaseModel."""
    def __init__(self, *args, **kwargs):
        """Initialize Review instance."""
        super().__init__(*args, **kwargs)
        # Add any specific attributes for Review here

