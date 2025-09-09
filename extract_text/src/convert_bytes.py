import io
import soundfile as sf
from logger.logger_to_elasic import Logger

logger = Logger.get_logger()


class ConvertBytes:

    def __init__(self, file_byte):
        self.file_byte = file_byte

    def convert_to_audio(self):
        try:
            like_file = io.BytesIO(self.file_byte)
            audio, sr = sf.read(like_file)
            logger.info("convert from bytes to file audio")
            return audio

        except Exception as e:
            logger.error(f"Convert failed {e}")
