import base64
from Crypto.Cipher import Blowfish


class CryptoUtil:
    def __init__(self):
        pass

    @staticmethod
    def decrypt(raw_text, password):
        text = base64.b64decode(raw_text)
        cipher = Blowfish.new(password)
        result = cipher.decrypt(text)
        return str(result)
