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

        self.new_account = Credentials("instagram","monginadee","@Mongina")
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        Credentials.list_account=[]


