import logging

# formatting the log message
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s--%(name)s--%(levelname)s--%(message)s",datefmt='%m/%d/%Y %H:%M:%S')

#The defined levels, in order of increasing severity. By default level is set to warning.
logging.debug("This is a Debug message.")
logging.info("This is an Info message.")
logging.warning("This is a Warning message.")
logging.error("This is an Error message.")
logging.critical("This is a Critical message.")
