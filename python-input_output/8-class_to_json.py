#!/usr/bin/python3
"""module efines a Python class-to-JSON function."""


def class_to_json(obj):
    """dictionary representation of a simple data structure."""
    return obj.__dict__