import logging

# This sets the root logger to write to stdout (your console).
# Your script/app needs to call this somewhere at least once.
# logging.basicConfig()

# By default the root logger is set to WARNING and all loggers you define
# inherit that value. Here we set the root logger to NOTSET. This logging
# level is automatically inherited by all existing and new sub-loggers
# that do not set a less verbose level.
# logging.root.setLevel(logging.NOTSET)

# The following line sets the root logger level as well.
# It's equivalent to both previous statements combined:
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('AdultUser.log')

c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

class AdultUser:
    def __init__(self, fullname,age,email) -> None:
        try:
            self.fullname = fullname
            self.age = age
            self.email = email
            logger.info(f"<AdultUser: {self.fullname}> created.")
        except Exception as e:
            logger.error(str(e))

     # using property decorator
     # a getter function
    @property
    def age(self):
        return self._age

    # a setter function
    @age.setter
    def age(self, value):
        if(value < 18):
            raise ValueError(f"Sorry {self.fullname} your age is below eligibility criteria")

        self._age = value

luke = AdultUser('Luke',23,"luke@gmail.com")
bryan = AdultUser('Bryan',3,"bryan@gmail.com")
