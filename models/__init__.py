from models.engine.file_storage import FileStorage
from . import storage

storage = FileStorage()
storage.reload()

