import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('logs.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s -  %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.setLevel(logging.INFO)

