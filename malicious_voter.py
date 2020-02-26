from voter import Voter


class MaliciousVoter(Voter):

    def vote(self):
        self._message = b'invalid'
        self.put_message_to_blokchain()
