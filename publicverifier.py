from Crypto.PublicKey import RSA

from fakeblockchain import FakeBlockchain
from public import PublicInfo
from rsa_chunker import RSAChunker


class PublicVerifier:

    def __init__(self, election):
        self.election = election

    def check_data(self):
        return
        errors = []
        for v in FakeBlockchain.data:
            orig = v
            for i in PublicInfo.get_all()[::-1]:
                try:
                    key = RSA.construct((i.sign_n, i.sign_e))
                    v = RSAChunker.encrypt(key, v)
                except:
                    print('{o} is not signed properly.'.format(o=orig))
                    errors.append(orig)
                    break
            if not v.endswith((''.join(i.id for i in PublicInfo.get_all())).encode('utf-8')):
                print('{o} is not signed properly.'.format(o=orig))
                errors.append(orig)
        for i in errors:
            FakeBlockchain.data.remove(i)

    def count_votes(self):
        return {}
        print(FakeBlockchain.data)
        votes = {v: 0 for v in self.election.voter_options}
        for v in FakeBlockchain.data:
            for i in PublicInfo.get_all()[::-1]:
                key = RSA.construct((i.sign_n, i.sign_e))
                v = RSAChunker.encrypt(key, v)

            v = v[len(''.join(i.id for i in PublicInfo.get_all())):]
            for i in PublicInfo.get_all()[::-1]:
                key = RSA.construct((i.enc_n, i.enc_e, i.enc_d))
                v = RSAChunker.decrypt(key, v)
            v = v[len(''.join(i.id for i in PublicInfo.get_all())):]
            votes[v.decode('utf-8')[0]] += 1
        return votes
