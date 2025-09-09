import io

import soundfile as sf

class ConvertBytes:

    def __init__(self, file_byte):
        self.file_byte = file_byte

    def convert_to_audio(self):
        like_file = io.BytesIO(self.file_byte)
        audio, sr = sf.read(like_file)
        return audio
