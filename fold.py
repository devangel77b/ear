import json
import logging



class Fold(object):
    def __init__(self):
        logging.debug("creating Fold object")
        return(None)

def read_fold(filename):
    logging.debug("reading Fold object from {0}".format(filename))
    return(json.load(filename))
