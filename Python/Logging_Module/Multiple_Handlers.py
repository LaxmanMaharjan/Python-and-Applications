import logging
#Creating logger objects
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
#Creating a Handler Objects
stream_Handler = logging.StreamHandler()
file_Handler = logging.FileHandler(f'{__name__}.txt')

#Attach handler to logger
log.addHandler(stream_Handler)
log.addHandler(file_Handler)

#Issues log message. Message goes to both handler
log.info("This is info message.")