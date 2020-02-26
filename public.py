class AuthorityPublicInfo:
    id = None

    sign_n = None
    sign_e = None

    enc_n = None
    enc_e = None
    enc_d = None

    sign = None


class InspectorPublicInfo:
    id = None

    sign_n = None
    sign_e = None

    enc_n = None
    enc_e = None
    enc_d = None

    sign = None


class PublicInfo:
    authority_public_info = None
    inspector_public_infos = []

    @staticmethod
    def get_all():
        return [PublicInfo.authority_public_info] + PublicInfo.inspector_public_infos

    @staticmethod
    def get_max_sign_n():
        return max([0] + [i.sign_n for i in PublicInfo.get_all() if i])

    @staticmethod
    def get_max_enc_n():
        return max([0] + [i.enc_n for i in PublicInfo.get_all() if i])
