import base64

class Decoder:

    def __init__(self, code):
        self.code = code

    def decoded_from_base64(self):
        base64_bytes = self.code.encode('ascii')
        decoded_bytes = base64.b64decode(base64_bytes)
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string

d = Decoder("R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT")
e = Decoder("RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==")
print(e.decoded_from_base64())