import json

def to_dict(obj:object):
    '''converts object to dict'''

    new_dict = {}
    for attr, value in obj.__dict__.items():
        new_dict[str(attr)] = value
    return new_dict

def load_file_data(filename):
    '''loads the json file data'''

    f = open(filename, "r",  encoding="utf-8")
    data = json.load(f)
    f.close()
    return data

def write_file_data(filename, data):
    '''writes data into json file'''

    f = open(filename, "w", encoding= "utf-8")
    f.write(data)
    f.close()