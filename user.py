class User:
    """
    creation of a new user class instance
    """
    users_list = []

    def __init__(self, username, password):

        '''
        __init__ method that helps us define the users objects properties

        Args:
            username: login's username for a new user
            password: login:s password for a new user
        '''
    
        self.username = username
        self.password = password

    def save_user (self):
      """
      A function that allows users to save their object properties
      """
      User.users_list.append(self)

    def delete_user(self):
        """
        A function that allows users to delete their object properties from the list.
        """
        User.users_list.remove(self)

    @classmethod
    def find_username(cls, username):
        """Find user by username"""
        for user in cls.users_list:
            if user.username == username:
                return user