import json

def get():
    return json.load(open('dict.json', 'r'))
