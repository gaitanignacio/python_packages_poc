# CLEAN EXAMPLE CODE TO MANAGE EXCEPTIONS

import logging
logger = logging.getLogger(__name__)

try:
    with open("./test.txt", 'r') as f:
        data = f.read()
        print(data)
except (SystemExit, KeyboardInterrupt, IOError, FileNotFoundError) as e:
    logger.error('Failed', exc_info=True)
    raise FileNotFoundError("Ni idea pibe")
except Exception as exception:
    logger.error('Failed to open file', exc_info=True)
finally:
    print("Finally!")
print("All Done")
