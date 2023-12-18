#!/usr/bin/python3
"""
Init Module for models package
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
