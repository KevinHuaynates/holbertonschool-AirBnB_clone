from models.base_model import BaseModel


class City(BaseModel):
    """Class City that from BaseModel."""
    def __init__(self, *args, **kwargs):
        """Initialize City instance."""
        super().__init__(*args, **kwargs)
