from configurations.mongodb_configuration import DbConnection
import gridfs
from logger.logger_to_elasic import Logger

logger = Logger.get_logger()


class DalMongo:

    def __init__(self, connection: DbConnection):
        self.connection = connection
        self.fs = gridfs.GridFS(self.connection.db)

    # Converting the file to binary and insert it into Mongo
    def insert_file(self, file_path, file_id):
        try:
            with open(file_path, 'rb') as f:
                file_id = self.fs.put(f, _id=file_id)
            logger.info(f"File stored with ID: {file_id}")
        except Exception as e:
            logger.error(f"Failed to insert file: {e}")

    def get_file_by_id(self, file_id):
        try:
            grid_out = self.fs.get(file_id)
            file_data = grid_out.read()
            logger.info(f"File with ID: {file_id} pull from mongo")
            return file_data
        except Exception as e:
            logger.error(f"Failed to get file: {e}")
