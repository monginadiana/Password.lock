import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    We are creating a class TestUser that defines test cases for the user class behaviours

    Args:
        unittest.Testcase: class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method that gives direction of how every other funtcion should run.
        '''
        self.new_user = User("Diana", "@Mongina")
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.users_list=[]
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Diana")
        self.assertEqual(self.new_user.password,"@Mongina")

    def test_save_user(self):
        '''
        test_save_user to check if we can save our user object to our users_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

    def test_delete_user(self):
        """
        delete_user to check if the user has being deleted from the users_list
        """
        self.new_user.save_user()
        new_user = User("Diana","@Mongina") 
        new_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.users_list),1)

    def test_find_username(self):
        """
        check whether the user account exists in the user accounts list
        """
        self.found_user = User.find_username("Diana")


        

if __name__ == '__main__':
    unittest.main()