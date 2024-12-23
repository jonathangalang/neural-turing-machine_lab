import logging
import sys

def configure():
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout, \
            format='%(asctime)s [%(levelname)s]: %(message)s')

def get_logger(name):
    return logging.getLogger(name)
