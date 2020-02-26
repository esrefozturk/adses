class RSAChunker:

    @staticmethod
    def encrypt(key, m, size=128):
        result = b''
        for i in range(0, len(m), size):
            result += key.encrypt(m[i:i + size], 1)[0]
        return result

    @staticmethod
    def decrypt(key, m, size=128):
        result = b''
        for i in range(0, len(m), size):
            result += key.decrypt(m[i:i + size])
        return result

    @staticmethod
    def blind(key, m, r, size=128):
        result = b''
        for i in range(0, len(m), size):
            result += key.blind(m[i:i + size], r)
        return result

    @staticmethod
    def unblind(key, m, r, size=128):
        result = b''
        for i in range(0, len(m), size):
            result += key.unblind(m[i:i + size], r)
        return result
