import pyperclip

class User:

    
    users_list = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def create_account(self):
        User.users_list.append(self)

    @classmethod
    def user_exist(cls, user_name, password):

       
        for user in cls.users_list:
            if user.user_name == user_name and user.password == password:
                return True
        return False

class Credentials:

credentials_list = []

    def __init__(self, account, username, password):

    self.account = account
        self.username = username
        self.password = password

    def save_credentials(self):

     Credentials.credentials_list.append(self)

    def delete_credentials(self):

    Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_account(cls, account):
       
for Credentials in cls.credentials_list:
            if Credentials.account == account:
                return Credentials

    @classmethod
    def credentials_exist(cls, account):
        
        for Credentials in cls.credentials_list:
            if Credentials.account == account:
                return True

        return False

    @classmethod
    def display_credentials(cls):
         
       
        return cls.credentials_list

    @classmethod
    def copy_password(cls, account):
        
    Credentials_found = Credentials.find_by_account(account)
    pyperclip.copy(Credentials_found.password)

        