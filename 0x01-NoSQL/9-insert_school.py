#!/usr/bin/env python3
"""
insert new document
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts new document to school colection
    """
    return mongo_collection.insert_one(kwargs).inserted_id
