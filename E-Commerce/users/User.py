from flask_login import UserMixin


class User(UserMixin, object):
    """
    User model
    """
    def __init__(self, **kwargs):
        """
        Constructor
        :param kwargs:
            id: user id
            username: username
            email: email
            password: password
        """
        self.id = kwargs.get('id', None)
        self.username = kwargs.get('username', None)
        self.email = kwargs.get('email', None)
        self.password = kwargs.get('password', None)

    def check_password(self, password):
        """
        Check password
        :param password: password to check
        :return: True if password is correct, False otherwise
        """
        return self.password == password

    def check_username_or_email(self, username_or_email):
        """
        Check username or email
        :param username_or_email: username or email to check
        :return: True if username or email is correct, False otherwise
        """
        return self.username == username_or_email or self.email == username_or_email
