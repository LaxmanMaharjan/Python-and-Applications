import re
import logging

# This sets the root logger to write to stdout (your console).
# Your script/app needs to call this somewhere at least once.
#logging.basicConfig()

# By default the root logger is set to WARNING and all loggers you define
# inherit that value. Here we set the root logger to NOTSET. This logging
# level is automatically inherited by all existing and new sub-loggers
# that do not set a less verbose level.
#logging.root.setLevel(logging.NOTSET)

# The following line sets the root logger level as well.
# It's equivalent to both previous statements combined:
logging.basicConfig(level=logging.DEBUG)


logger = logging.getLogger(__name__)
# Create handlers
# c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('User.log')

# c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
# logger.addHandler(c_handler)
logger.addHandler(f_handler)

class User:
    def __init__(self, fullname,age,email) -> None:
        try:
            self.fullname = fullname
            self.age = age
            self.email = email
            logger.info(f"<User: {self.fullname}> created.")

        except Exception as e:
            logger.error(str(e))

     # using property decorator
     # a getter function
    @property
    def email(self):
        return self._email

    # a setter function
    @email.setter
    def email(self, value):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.search(regex, value):
            raise ValueError(f"{self.fullname} please provide valid email.")
        self._email = value

luke = User('Luke',23,"luke@gmail.com")
bryan = User('Bryan',3,"bryan@gmail.com")

print(logger)
