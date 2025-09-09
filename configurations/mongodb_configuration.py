import os
import pymongo
from pymongo.errors import PyMongoError
from logger.logger_to_elasic import Logger
from configurations.config import *

logger = Logger.get_logger()


class DbConnection:
    def __init__(self):

        try:
            self.client = pymongo.MongoClient(
                host=MONGO_HOST,
                port=int(MONGO_PORT),
                username=MONGO_USER,
                password=MONGO_PASSWORD,
                authSource=AUTH_DB
            )

            self.db = self.client[MONGO_DB]
        except PyMongoError as e:
            logger.error(f"MongoDB connection error: {e}")
            raise
