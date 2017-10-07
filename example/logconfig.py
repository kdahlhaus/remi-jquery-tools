import logging

# options are here:
#   https://docs.python.org/3/library/logging.html#formatter-objects
formatter = logging.Formatter('%(levelname)8s %(name)s %(pathname)s %(funcName)s | %(message)s')

def configure_logger_with_name(logger_name, level=logging.DEBUG):
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger = logging.getLogger(logger_name)
    logger.addHandler(ch)
    logger.setLevel(level)
