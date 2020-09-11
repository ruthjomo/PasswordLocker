import unittest
from locker import User
from locker import Credentials
import pyperclip

class TestUsers(unittest.TestCase):

    
    

    def tearDown(self):

       
        User.users_list = []

    def setUp(self):

        
        self.new_user = User("Ruth", "Ruth19") 


    def test_init(self):

        self.assertEqual(self.new_user.user_name, "Kelvin")
        self.assertEqual(self.new_user.password, "Kelvin78")

    def test_create_account(self):

        self.new_user.create_account()
        self.assertEqual(len(User.users_list), 1)

    def test_save_multiple_accounts(self):

       

        self.new_user.create_account()
        test_user = User("Kendrick", "Kendrick19") #new user
        test_user.create_account()
        self.assertEqual(len(User.users_list), 2)

    def test_account_exists(self):

        

        self.new_user.create_account()
        test_user = User("Kendrick", "Kendrick19")
        test_user.create_account()

        user_exists = User.user_exist("Kendrick", "Kendrick19")

        self.assertTrue(user_exists)

class TestCredentials(unittest.TestCase):

  
    def tearDown(self):

       
        Credentials.credentials_list=[]

    def setUp(self):
        
        self.new_credentials = Credentials("Instagram","Rupy Marloney","newpassword") # create credentials object

    def test_init(self):

       

        self.assertEqual(self.new_credentials.account,"Instagram")
        self.assertEqual(self.new_credentials.username,"Rupy Marloney")
        self.assertEqual(self.new_credentials.password,"newpassword")

    def test_save_credentials(self):

      
        self.new_credentials.save_credentials() 
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):

          
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test","username","newpass") 
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):

      
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","username","newpass") 
        test_credentials.save_credentials()
        
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_credentials_exists(self):

       

        self.new_credentials.save_credentials()
        test_credentials = Credentials('Test', 'username', 'newpass')
        test_credentials.save_credentials()

        Credentials_exists = Credentials.credentials_exist('Test')

        self.assertTrue(Credentials_exists)

    def test_display_all_credentials(self):

      

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    def test_copy_password(self):

       

        self.new_credentials.save_credentials()
        Credentials.copy_password('Instagram')

        self.assertEqual(self.new_credentials.password,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()




