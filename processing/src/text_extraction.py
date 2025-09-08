from faster_whisper import WhisperModel

class TextExtraction:

    def __init__(self):
        self.model = WhisperModel("base", device="cpu", compute_type="int8")

    def extract_text_from_a_file(self, file_path):
        text = ""
        segments, info = self.model.transcribe(file_path, beam_size=5)
        for seg in segments:
            text += seg.text

        return text
