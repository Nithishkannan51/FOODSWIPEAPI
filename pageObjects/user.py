from utilities.conf import Conf


class user:
    userid=""
    user_token=""

    @staticmethod
    def get_create_user_payload():
        payload = {
            "name": Conf.user_name,
            "email": Conf.user_email,
            "password": Conf.user_password,
            "age": Conf.user_age
        }
        return payload

    @staticmethod
    def get_login_user_invalid_payload():
        payload = {
            "email": Conf.user_email_invalid,
            "password": Conf.user_password
        }
        return payload

    @staticmethod
    def get_login_user_payload():
        payload = {
            "email": Conf.user_email,
            "password": Conf.user_password
        }
        return payload

    @staticmethod
    def get_update_user_payload():
        payload = {
            "age": Conf.user_updated_age
        }
        return payload



