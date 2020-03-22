import logging

#Create and configure logger

LOG_FORMAT = "%(levelname)s : %(asctime)s  From proccess %(process)s %(processName)s and thread %(thread)s %(threadName)s - %(message)s"

logging.basicConfig(filename="./test.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w',
                    datefmt="%Y-%m-%d %H:%M:%S")

logger=logging.getLogger()


# Test Logger

logger.debug("Testing critical logging")
logger.info("Testing critical logging")
logger.warning("Testing critical logging")
logger.error("Testing critical logging")
logger.critical("Testing critical logging")