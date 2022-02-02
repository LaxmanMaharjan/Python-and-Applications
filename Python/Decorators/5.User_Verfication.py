import functools
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class AnonymousUser:
    def __init__(self, username, email):
        self.username = username
        self.email = email

def user_verification(fxn):
    @functools.wraps(fxn)
    def inner(user,*args,**kwargs):
        #verifies the user
        if isinstance(user,User):
            return fxn(user,*args,**kwargs)
        else:
            raise TypeError("A valid User is required to use this.")
    return inner
