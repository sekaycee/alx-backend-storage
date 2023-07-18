#!/usr/bin/env python3
''' task 8: list all docs in Python '''


def list_all(mongo_collection):
    ''' list all documents in a collection. '''
    docs = []
    for doc in mongo_collection.find():
        docs.append(doc)
    return docs
