from official import Official
from public import PublicInfo, AuthorityPublicInfo


class Authority(Official):

    def broadcast_public_info(self):
        a = AuthorityPublicInfo()

        a.id = self.id

        a.sign_n = self.sign_key.n
        a.sign_e = self.sign_key.e

        a.enc_n = self.enc_key.n
        a.enc_e = self.enc_key.e

        a.sign = self.sign

        PublicInfo.authority_public_info = a

    def broadcast_private_info(self):
        PublicInfo.authority_public_info.enc_d = self.enc_key.d


def main():
    pass


if __name__ == '__main__':
    main()
