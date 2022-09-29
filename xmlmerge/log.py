"""
Application logging operations
"""

import logging
from sys import version_info
from functools import lru_cache


class SingletonMeta(type):
    __call__ = lru_cache(maxsize=None)(type.__call__)


class Logger(metaclass=SingletonMeta):
    """
    Logger with singleton metaclass
    """
    format = '%(levelname)-8s | %(asctime)s | %(module)-8s:%(lineno)-4d | %(message)s'
    log = logging.basicConfig(level=logging.INFO, format=format) or logging.getLogger()

    def __init__(self, level=logging.INFO) -> None:
        self.level = level
        self.log = self.get_log

    @property
    def get_log(self):
        """
        Fetching logger with logging level
        """
        logging.basicConfig(level=self.level, format=format)
        return logging.getLogger()