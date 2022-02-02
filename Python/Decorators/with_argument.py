import json
import functools
def json_output(decorated_ = None, indent = None, sort_keys = None):
    """
    Decorator with argument
    :param decorated_:
    :param indent:
    :param sort_keys:
    :return:
    """
    if decorated_ and (indent or sort_keys):
        raise RuntimeError("Unexpected Arguments")
    def decorated_by(method):
        @functools.wraps(method)
        def wrapper(*args,**kwargs):
            result = method(*args,**kwargs)
            return json.dumps(result,indent=indent,sort_keys=sort_keys)
        return wrapper

    if decorated_:
        return decorated_by(decorated_)
    else:
        return decorated_by

@json_output(sort_keys=True)
def test():
     return {
    'fname': 'Joe',
    'lname': 'Fonebone',
    'age': 51,
    'spouse': 'Edna',
    'children': ['Ralph', 'Betty', 'Joey'],
    'pets': {'dog': 'Fido', 'cat': 'Sox'},
    'married':True,
    'sons':None
    }
print(test())