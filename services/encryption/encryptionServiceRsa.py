from services.encryption.encryptionBase import EncryptionBase

class EncryptionServiceRsa(EncryptionBase):
    def encrypt(self, data: bytes, key: str) -> bytes:
        return data

    def decrypt(self, data: bytes, key: str) -> bytes:
        return data

    def getExtension(self) -> str:
        return ".rsa"
