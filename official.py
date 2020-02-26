from Crypto.PublicKey import RSA

from rsa_chunker import RSAChunker


class Official():
    id = None

    sign_key = None

    enc_key = None

    def generate_random_id(self):
        self.id = self.election.generate_random_id()

    def __init__(self, election):
        self.election = election
        self.generate_random_id()

    def generate_sign_key_pairs(self):
        key = RSA.generate(1024)
        self.sign_key = key

    def generate_enc_key_pairs(self):
        key = RSA.generate(1024)
        print('n\t:\t', key.n)
        print('e\t:\t', key.e)
        print('d\t:\t', key.d)

        self.enc_key = key

    def broadcast_public_info(self):
        pass

    def broadcast_private_info(self):
        pass

    def sign(self, message):
        return RSAChunker.decrypt(self.sign_key, message)


def main():
    pass


if __name__ == '__main__':
    main()
