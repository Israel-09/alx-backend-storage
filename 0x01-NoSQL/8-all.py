#!/usr/bin/env python3
"""
retrieves all document in a collection
"""


def list_all(mongo_collection):
    """
    return all document in a collection
    """
    schools = mongo_collection.find()
    return schools if schools else []
