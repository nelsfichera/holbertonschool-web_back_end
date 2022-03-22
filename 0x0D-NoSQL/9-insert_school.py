#!/usr/bin/env python3
'''inserts a new argument from kwargs but with python'''


def insert_school(mongo_collection, **kwargs):
    '''does the thing'''
    doc_id = mongo_collection.insert(kwargs)
    return doc_id