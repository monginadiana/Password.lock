import unittest
from account import Credentials

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):

        '''
        Set up method to run before each test cases.
        '''

        self.new_account = Credentials("Instagram","monginadee","@Mongina")
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        Credentials.list_account=[]
    def test_init(self):

        '''
        test_init test case to test if the object is initialized correctly
        '''

        self.assertEqual(self.new_account.account_name,"Instagram")
        self.assertEqual(self.new_account.username,"monginadee") 
        self.assertEqual(self.new_account.password,"@Mongina")
    
    def test_save_account(self):

        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''

        self.new_account.save_account()
        self.assertEqual(len(Credentials.list_account),1)
if __name__ == '__main__':
    unittest.main()
    



