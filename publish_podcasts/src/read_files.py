from pathlib import Path, PurePosixPath
import datetime


class ReadFiles:

    def __init__(self, path):
        self.path = Path(path)

    def read_metadata_on_file(self):
        files = []
        for subdir in self.path.iterdir():
            file = {}
            path = PurePosixPath(subdir)
            file_size = subdir.stat().st_size
            file_name = subdir.name
            created_at = subdir.stat().st_ctime
            to_time = str(datetime.datetime.fromtimestamp(created_at))
            file["path"] = path
            file["file_size"] = file_size
            file["file_name"] = file_name
            file["created_at"] = to_time
            files.append(file)

        return files



