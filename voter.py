from Crypto.PublicKey import RSA

from fakeblockchain import FakeBlockchain
from public import PublicInfo
from rsa_chunker import RSAChunker
import re

def tex_escape(text):
    """
        :param text: a plain text message
        :return: the message escaped to appear correctly in LaTeX
    """
    conv = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
        '<': r'\textless{}',
        '>': r'\textgreater{}',
    }
    regex = re.compile('|'.join(re.escape(unicode(key)) for key in sorted(conv.keys(), key = lambda item: - len(item))))
    return regex.sub(lambda match: conv[match.group()], text)

class Voter:
    _id = None
    _vote = None
    _message = None
    _blinding_factors = {}

    def generate_random_id(self):
        self._id = self.election.generate_random_id()

    def generate_random_vote(self):
        self._vote = self.election.generate_random_vote()

    def __init__(self, election):
        self.election = election
        self.generate_random_id()
        self.generate_random_vote()

    def generate_message(self):
        self._message = '{v}{i}'.format(
            i=''.join(i.id for i in PublicInfo.get_all()),
            v=self._vote
        )
        self._message = self._message.encode('utf-8')

    def enc_message(self):
        for i in PublicInfo.get_all():
            key = RSA.construct((i.enc_n, i.enc_e))
            self._message = RSAChunker.encrypt(key, self._message)
        for i in PublicInfo.get_all():
            self._message = self._message + i.id.encode('utf-8')

    def set_blinding_factors(self):
        for i in PublicInfo.get_all():
            self._blinding_factors[i.id] = i.sign_n - 1

    def sign_message(self):

        for i in PublicInfo.get_all():
            key = RSA.construct((i.sign_n, i.sign_e))

            blinded = RSAChunker.blind(key, self._message, self._blinding_factors[i.id])
            sign = i.sign(blinded)

            sign = RSAChunker.unblind(key, sign, self._blinding_factors[i.id])

            if RSAChunker.encrypt(key, sign) == self._message:
                self._message = sign
            else:
                raise Exception('NOOOOOOOOOOOOOOO')

    def put_message_to_blokchain(self):
        FakeBlockchain.data.append(self._message)

    def vote(self):
        print('Creating Voter')
        print('v\t:\t', self._vote[0].encode('utf-8'))
        print('r\t:\t', self._vote[1:].encode('utf-8'))
        print('id\t:\t', (''.join(i.id for i in PublicInfo.get_all())).encode('utf-8'))
        self.generate_message()
        print('m\t:\t', self._message)
        self.enc_message()
        print('m_e\t:\t', repr(self._message))
        self.set_blinding_factors()
        self.sign_message()
        print('m_s\t:\t', self._message)
        self.put_message_to_blokchain()


def main():
    pass


if __name__ == '__main__':
    main()
