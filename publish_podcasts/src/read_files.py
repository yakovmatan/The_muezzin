from pathlib import Path, PurePosixPath
import datetime
from logger.logger_to_elasic import Logger

logger = Logger.get_logger()

class ReadFiles:

    def __init__(self, path):
        self.path = Path(path)

    def read_metadata_on_file(self):
        logger.info("start to get metadata on files")
        files = []
        for subdir in self.path.iterdir():
            if not subdir.is_file():
                continue
            file = {}
            path = str(PurePosixPath(subdir)) #
            file_size = str(subdir.stat().st_size)
            file_name = subdir.name
            created_at = subdir.stat().st_ctime
            to_time = str(datetime.datetime.fromtimestamp(created_at))
            file["path"] = path
            file["file_size"] = file_size
            file["file_name"] = file_name
            file["created_at"] = to_time
            files.append(file)
        logger.info("finish to get metadata on files")
        return files



