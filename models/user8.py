from models.base_model import BaseModel


class User(BaseModel):
    """User class for AirBnB project."""
    def __init__(self, *args, **kwargs):
        """Initialize a new User instance."""
        super().__init__(*args, **kwargs)
        # Add user-specific attributes here
