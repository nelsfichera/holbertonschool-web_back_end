#!/usr/bin/env python3
'''updates the database but with pymongo'''


def update_topics(mongo_collection, name, topics):
    '''does the thing'''
    query = {"name": name}
    new_val = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_val)