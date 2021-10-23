class Credentials:

    '''
    class that generates new instances of new accounts and their credentials
    '''

    list_account=[]

    def __init__(self,account_name,username,password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            account_name: new user  social account name
            username: new user username
            password: new user password
        '''
        self.account_name=account_name
        self.username=username
        self.password=password

    def save_account(self):

        '''
        save_account method saves accounts objects into the contact_list
        '''
        Credentials.list_account.append(self)

    def delete_account(self):
        '''
        deletes save accounts from the account list
        '''
        Credentials.list_account.remove(self)
    @classmethod
    def display_accounts(cls):
        '''
        This method displays saved credentials
        '''

        return cls.list_account
    
