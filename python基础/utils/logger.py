# -*- coding: utf-8 -*-
"""
====================================
@File Name ：logger.py
@Time ： 2022/11/17 15:25
@Program IDE ：PyCharm
@Create by Author ： stone
@Describe：logger工具工具类
====================================
"""

import logging
import time


class Logger(object):
    def __init__(self, path, name, level=logging.DEBUG):
        self.time = time.strftime("%y-%m-%d")

        self.filename = path + name + '-' + self.time + ".log"
        self.logger = logging.getLogger(self.filename)
        self.logger.setLevel(level)
        fmt = logging.Formatter('[%(asctime)s %(threadName)s]\
                [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        fh = logging.FileHandler(self.filename,encoding='utf-8')
        fh.setFormatter(fmt)
        fh.setLevel(level)
        self.logger.addHandler(fh)

    def debug(self, message):
        """
        This is debug
        """
        self.logger.debug(message)

    def info(self, message):
        """
        This is info
        """
        self.logger.info(message)

    def warn(self, message):
        """
        This is warn
        """
        self.logger.warn(message)

    def error(self, message):
        """
        This is error
        """
        self.logger.error(message)

    def critical(self, message):
        """
        This is critical
        """
        self.logger.critical(message)

