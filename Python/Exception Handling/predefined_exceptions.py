class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg = msg
class TooOldException(Exception):
    def __init__(self,msg):
        self.msg = msg
def find_partner(age):
    if age>60:
        raise TooOldException("Your age crossed the marriage age.")
    elif age<18:
        raise TooYoungException("You are too young for Marriage.")
    else:
        print("Searching for a Match")
find_partner(11)
