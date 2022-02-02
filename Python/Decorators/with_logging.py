import time
import logging
import functools
def logged(method):
    """
    Causes the decorated function to run and log the result and some diagnostic info
    :param method:
    :return:
    """
    @functools.wraps(method)
    def inner(*args,**kwargs):
        #Record start time
        start = time.time()

        result = method(*args,**kwargs)

        #time after completion of method run
        end = time.time()

        delta = end - start

        logger = logging.getLogger("decorator.logged")
        logger.setLevel(logging.INFO)
        stream_handler = logging.StreamHandler()
        logger.addHandler(stream_handler)
        logger.info(f"Execution Time of {method.__name__} is {delta} seconds")
        return  result
    return inner

@logged
def heavy_function():
    time.sleep(2)

heavy_function()

