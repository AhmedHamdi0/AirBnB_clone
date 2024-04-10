#!/usr/bin/python3
"""Initializes a FileStorage object and reloads data from storage."""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
