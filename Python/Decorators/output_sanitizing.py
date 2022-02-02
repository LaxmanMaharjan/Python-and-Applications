import functools
import json
people = {
    'fname': 'Joe',
    'lname': 'Fonebone',
    'age': 51,
    'spouse': 'Edna',
    'children': ['Ralph', 'Betty', 'Joey'],
    'pets': {'dog': 'Fido', 'cat': 'Sox'}
    }
print(type(json.dumps(people)))

def json_output(decorated):
    """Run the decorated function, serialize the result of that function
    to JSON, and return the JSON string.
    """
    @functools.wraps(decorated)
    def wrapper(*args,**kwargs):
        result = decorated(*args,**kwargs)
        return json.dumps(result)
    return wrapper
@json_output
def do_nothing():
    return {'status':'done'}
print(do_nothing())