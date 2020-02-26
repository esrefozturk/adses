from random import choice, randint
from string import ascii_uppercase

from authority import Authority
from fakeblockchain import FakeBlockchain
from inspector import Inspector
from public import PublicInfo
from publicverifier import PublicVerifier
from voter import Voter


class Election:

    def generate_random_vote(self):
        return '{v}{r}'.format(
            v=self.voter_options[randint(0, len(self.voter_options) - 1)],
            r="".join(choice(ascii_uppercase) for _ in range(self.vote_length - 1))
        )

    def generate_random_id(self):
        return "".join(choice(ascii_uppercase) for _ in range(self.id_length))

    def create_authority(self):
        self.authority = Authority(self)

    def create_inspectors(self):
        self.inspectors = []
        for i in range(len(self.voter_options)):
            self.inspectors.append(Inspector(self))

    def create_officials(self):
        self.create_authority()
        self.create_inspectors()

    def create_voters(self):
        self.voters = []
        for i in range(self.voter_count):
            self.voters.append(Voter(self))

    def generate_enc_key_pairs(self):
        print('Creating Authority')
        self.authority.generate_enc_key_pairs()
        for i in self.inspectors:
            print('Creating Inspector')
            i.generate_enc_key_pairs()

    def generate_sign_key_pairs(self):
        self.authority.generate_sign_key_pairs()
        for i in self.inspectors:
            i.generate_sign_key_pairs()

    def broadcast_public_info(self):
        self.authority.broadcast_public_info()
        for i in self.inspectors:
            i.broadcast_public_info()

    def broadcast_private_info(self):
        self.authority.broadcast_private_info()
        for i in self.inspectors:
            i.broadcast_private_info()

    def __init__(self, voter_count=10, voter_options=None):
        FakeBlockchain.data = []
        PublicInfo.authority_public_info = None
        PublicInfo.inspector_public_infos = []
        self.voter_options = voter_options
        if self.voter_options is None:
            self.voter_options = ['A', 'B']
        print('Vote options:', self.voter_options)
        self.voter_count = voter_count
        self.public_verifier = PublicVerifier(self)

        self.id_length = 16

        self.vote_length = 16

        self.message_length = self.id_length * (len(self.voter_options) + 1) + self.vote_length + 1

        self.create_officials()
        self.create_voters()
        self.generate_enc_key_pairs()
        self.generate_sign_key_pairs()
        self.broadcast_public_info()

        for i in self.voters:
            i.vote()
            self.public_verifier.check_data()

        from malicious_voter import MaliciousVoter
        m = MaliciousVoter(self)
        m.vote()
        self.public_verifier.check_data()

        self.broadcast_private_info()
        print(self.public_verifier.count_votes())


def main():
    Election()


if __name__ == '__main__':
    main()
