import logging
# create logger with 'debug_test'
logger = logging.getLogger('debug_test')
logger.setLevel(logging.DEBUG)
for h in logger.handlers[:]:
    logger.removeHandler(h)
    h.close()
# create file handler which logs even debug messages
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('Watch debug log!')
logger.info('Watch info log!')
logger.warning('Watch warning log!')
logger.error('Watch error log!')
logger.critical('Watch critical log!')