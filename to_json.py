import json

def to_json(func):
    def wrapped(*args, **kwargs):
        result = json.dumps(func(*args, **kwargs))
        return result
    wrapped.__name__=func.__name__
    return wrapped


@to_json
def ret_nothing():
    return None