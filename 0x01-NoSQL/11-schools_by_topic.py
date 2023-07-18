#!/usr/bin/env python3
''' task 11: where can I learn python '''


def schools_by_topic(mongo_collection, topic):
    ''' return the list of school having a specific topic. '''
    return list(mongo_collection.find({'topics': topic}))
