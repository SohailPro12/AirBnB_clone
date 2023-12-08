#!/usr/bin/python3
""" storage """
from models.engine.file_storage import FileStorage


"""
Create a unique FileStorage instance for our application
"""
storage = FileStorage()
storage.reload()
