# Exceptions
import time
import logging

# Create logger
logging.basicConfig(filename = "mylog_01.log", level = logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path: str):
    """Returns file contents"""
    start_time = time.time()

    try:
        f = open(path, "rb")
        data = f.read()
        logger.info("File {name} has been opened".format(name = path))
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        pass
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("File operations required {time} seconds".format(time = dt))

data = read_file_timed("d:\\Downloads\\Image 2019-01-31 at 06.36.00.jpeg")
