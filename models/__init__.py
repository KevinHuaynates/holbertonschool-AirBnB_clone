from models.engine.file_storage import FileStorage

def initialize_storage():
    storage = FileStorage()
    storage.reload()

