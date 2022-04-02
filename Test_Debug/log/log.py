import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG, filename='blue_ox.log')
fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=fmt)

logging.debug("Looks like rain")
logging.info("And hail")
logging.warning("Did I hear thunder?")
logging.error("Was that ligthning?")
logging.critical("Stop fencing and get inside!")

# logging.basicConfig(level=logging.DEBUG)
logging.debug("It's raining again")

logger = logging.getLogger('bunyan')
logger.debug('Timber!')
logger.warning("I need my axe")