import functools
import json
class JsonOutputError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg


def json_output(decorated):
    @functools.wraps(decorated)
    def wrapper(*args,**kwargs):
        try:
            result = decorated(*args,**kwargs)
        except JsonOutputError as msg:
            result={
                'status':"Error",
                'Message':str(msg)
            }
        return json.dumps(result)
    return wrapper

@json_output
def output():
    raise JsonOutputError("hello")