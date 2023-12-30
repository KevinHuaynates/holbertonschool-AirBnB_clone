from models.base_model import BaseModel

class State(BaseModel):
    """Class State that inherits from BaseModel."""
    def __init__(self, *args, **kwargs):
        """Initialize State instance."""
        super().__init__(*args, **kwargs)
        # Add any specific attributes for State here

