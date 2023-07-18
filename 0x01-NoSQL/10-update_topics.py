#!/usr/bin/env python3
''' task 10: change school topics '''


def update_topics(mongo_collection, name, topics):
    ''' change all topics of a collection's document based on the name. '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
