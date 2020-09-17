import unittest
from locker import User
from locker import Credentials
import pyperclip

class TestUsers(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:

    unittest.TestCase: TestCase class that helps in creating test cases

    '''

    def tearDown(self):

        '''
        tearDown method to run after each test  cases.

        '''
        User.users_list = []

    def setUp(self):

        '''
        Set up method to run before each test cases.

        '''
        self.new_user = User("Ruth", "Ruth78") # create user object


    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly

        '''

        self.assertEqual(self.new_user.user_name, "Ruth")
        self.assertEqual(self.new_user.password, "Ruth78")

    def test_create_account(self):

        '''
        test_create_account test case to test if the user object is saved into
        the user list

        '''

        self.new_user.create_account()
        self.assertEqual(len(User.users_list), 1)

    def test_save_multiple_accounts(self):

        '''
        test_save_multiple_user to check if we can save multiple users
        objects to our user_list
        
        '''

        self.new_user.create_account()
        test_user = User("Kendrick", "Kendrick78") #new user
        test_user.create_account()
        self.assertEqual(len(User.users_list), 2)

    def test_account_exists(self):

        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        
        '''

        self.new_user.create_account()
        test_user = User("Kendrick", "Kendrick78")
        test_user.create_account()

        user_exists = User.user_exist("Kendrick", "Kendrick78")

        self.assertTrue(user_exists)

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def tearDown(self):

        '''
        tearDown method run after each test cases.
        '''
        Credentials.credentials_list=[]

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Instagram","RupyMarloney","newpassword") # create credentials object

    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account,"Instagram")
        self.assertEqual(self.new_credentials.username,"RupyMarloney")
        self.assertEqual(self.new_credentials.password,"newpassword")

    def test_save_credentials(self):

        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):

            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test","username","newpass") # new credential
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):

        '''
        test_delete_credentials to test if we can remove a credential from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","username","newpass") # new credentials
        test_credentials.save_credentials()
        
        self.new_credentials.delete_credentials()# Deleting a credential object
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_credentials_exists(self):

        '''
        test to return a boolean if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials('Test', 'username', 'newpass')
        test_credentials.save_credentials()

        Credentials_exists = Credentials.credentials_exist('Test')

        self.assertTrue(Credentials_exists)

    def test_display_all_credentials(self):

        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    def test_copy_password(self):

        '''
        test to confirm that we are copying the password from a found account
        '''

        self.new_credentials.save_credentials()
        Credentials.copy_password('Instagram')

        self.assertEqual(self.new_credentials.password,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()






        