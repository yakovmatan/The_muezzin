from configurations.mongodb_configuration import DbConnection
import gridfs
from logger.logger import get_logger

log = get_logger()

class DalMongo:

    def __init__(self, connection: DbConnection):
        self.connection = connection
        self.fs = gridfs.GridFS(self.connection.db)

    #Converting the file to binary and insert it into Mongo
    def insert_file(self, file_path, file_id):
        with open(file_path, 'rb') as f:
            file_id = self.fs.put(f, _id=file_id)
        log.info(f"File stored with ID: {file_id}")