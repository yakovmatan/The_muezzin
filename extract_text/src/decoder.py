import base64

class Decoder:

    def __init__(self, code):
        self.code = code

    # Base64 encryption converter
    def decoded_from_base64(self):
        base64_bytes = self.code.encode('ascii')
        decoded_bytes = base64.b64decode(base64_bytes)
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string