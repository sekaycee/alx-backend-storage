#!/usr/bin/env python3
''' task 9: insert a document in Python '''


def insert_school(mongo_collection, **kwargs):
    ''' insert a new document in a collection. '''
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
