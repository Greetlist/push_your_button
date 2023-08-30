import logging
import os
import datetime as dt

class Logger:
    log_dir = os.path.dirname(__file__)
    os.makedirs(log_dir)
    log_filename = 'hunter_{}.log'.format(dt.datetime.now().strftime('%Y-%m-%d-%H%M%S'))
    logger = logging.getLogger(log_filename)

    logger.setLevel(logging.INFO)
    if not logger.handlers:
        formatter = logging.Formatter('[%(filename)s %(lineno)s]| %(message)s')
        file_handler = logging.FileHandler(os.path.join(log_dir, log_filename))
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    @staticmethod
    def info(msg):
        Logger.logger.info(msg)
        Logger.logger.handlers[0].flush()

    @staticmethod
    def warning(msg):
        Logger.logger.warning(msg)
        Logger.logger.handlers[0].flush()

    @staticmethod
    def error(msg):
        Logger.logger.error(msg)
        Logger.logger.handlers[0].flush()