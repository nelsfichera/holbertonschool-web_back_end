#!/usr/bin/env python3
'''Lists all documents in db but with python'''


def list_all(mongo_collection):
    '''does the thing'''
    documents = mongo_collection.find()

    if documents.count == 0:
        return []
    return documents