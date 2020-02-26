from official import Official
from public import InspectorPublicInfo, PublicInfo


class Inspector(Official):

    def broadcast_public_info(self):
        a = InspectorPublicInfo()

        a.id = self.id

        a.sign_n = self.sign_key.n
        a.sign_e = self.sign_key.e

        a.enc_n = self.enc_key.n
        a.enc_e = self.enc_key.e

        a.sign = self.sign

        PublicInfo.inspector_public_infos.append(a)

    def broadcast_private_info(self):
        for i in range(len(PublicInfo.inspector_public_infos)):
            if PublicInfo.inspector_public_infos[i].id == self.id:
                break
        PublicInfo.inspector_public_infos[i].enc_d = self.enc_key.d


def main():
    pass


if __name__ == '__main__':
    main()
