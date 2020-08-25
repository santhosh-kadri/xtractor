import logging
import logging.config
from datetime import datetime
from logging.handlers import RotatingFileHandler



class Logger:
    def __init__(self, class_name):
        __file_name = datetime.now().strftime("%Y-%m-%d")
        self.__logger = None
        self.__logger = logging.getLogger(class_name)
        self.__logger.setLevel('DEBUG')
        __log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        __formatter = logging.Formatter(__log_format)
        __file_handler = RotatingFileHandler(f'{__file_name}.log', maxBytes=5000, backupCount=10)
        __file_handler.setFormatter(__formatter)

        # logger.info("I am a separate Logger")

        __console_handler = logging.StreamHandler()
        __formatter = logging.Formatter(__log_format)
        __console_handler.setFormatter(__formatter)

        self.__logger.addHandler(__file_handler)
        self.__logger.addHandler(__console_handler)

    def debug(self, log_msg):
        self.__logger.debug(log_msg)

    def info(self, log_msg):
        self.__logger.info(log_msg)

    def warning(self, log_msg):
        self.__logger.warning(log_msg)

    def error(self, log_msg):
        self.__logger.error(log_msg, exc_info=True)

    def critical(self, log_msg):
        self.__logger.critical(log_msg)



