from services.encryption.encryptionBase import EncryptionBase

class EncryptionServiceNone(EncryptionBase):
    def encrypt(self, data: bytes, key: str) -> bytes:
        return data

    def decrypt(self, data: bytes, key: str) -> bytes:
        return data

    def getExtension(self) -> str:
        return ""
