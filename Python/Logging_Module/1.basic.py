"""
This python file demonstrates creating log file and understanding logging levels
"""
import logging
#logging.basicConfig(filename="basic.log",level=logging.WARNING)
logging.basicConfig(filename="basic.log",level=logging.DEBUG,format='%(asctime)s%(levelname)s:%(message)s')
logging.debug("This is Debug Message.")
logging.info("This is info Messsage.")
logging.warning("This is warning Message.")
logging.error("This is Error Message.")
logging.critical("This is Critical Message.")

#writing exception to the log file
#
# try:
#     x = int(input("Enter the value of x:"))
#     y = int(input("Enter the value of y:"))
#     x/y
# except ZeroDivisionError as msg:
#     logging.exception(msg)
# except ValueError as msg:
#     logging.exception(msg)
# finally:
#     logging.info("Request completed.")
