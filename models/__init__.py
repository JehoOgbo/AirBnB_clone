#!/usr/bin/python3
"""
Create a unique FileStorage instance for your application
"""
__all__ = ['base_model']
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
