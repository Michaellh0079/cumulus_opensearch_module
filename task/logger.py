import logging
import os
from cumulus_logger import CumulusLogger


class MyLogger:
    info = print
    warning = print
    error = print
    """
    Class used for logging
    """
    pass


ops_logger = CumulusLogger(name='Open-Search-Lambda', level=logging.INFO) \
    if os.getenv('enable_logging', 'false').lower() == 'true' else MyLogger()

if __name__ == '__main__':
    pass
