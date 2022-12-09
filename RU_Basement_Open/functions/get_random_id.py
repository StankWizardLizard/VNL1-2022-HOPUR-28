import uuid

def get_random_id():
    """ Returns a unique ID"""
    return str(uuid.uuid1())