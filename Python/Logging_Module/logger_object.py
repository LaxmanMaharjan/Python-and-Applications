import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
log.addHandler(stream_handler)

log.debug("This is Debug Message.")
log.info("This is info Messsage.")
log.warning("This is warning Message.")
log.error("This is Error Message.")
log.critical("This is Critical Message.")