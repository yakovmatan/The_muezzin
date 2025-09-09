from faster_whisper import WhisperModel

from logger.logger_to_elasic import Logger

logger = Logger.get_logger()


class TextExtraction:

    def __init__(self):
        """
        Loading the model
        base = Medium model (good balance between speed and accuracy)
        device="cpu" -> will run on the CPU
        compute_type="int8" -> Uses less memory, slightly less accuracy but much faster
        """
        self.model = WhisperModel("base", device="cpu", compute_type="int8")

    def extract_text_from_a_file(self, file_path):
        try:
            text = ""
            # Runs transcription on an audio file
            segments, info = self.model.transcribe(file_path, beam_size=5)
            for seg in segments:
                text += seg.text
            logger.info("extract text from file")
            return text

        except Exception as e:
            logger.error(f"Extracting text from file failed {e}")
