 
from locker import User
from locker import Credentials
import secrets
import string

def create_account(user_name, password):
    '''
    a function to create a new user account
    '''

    new_user = User(user_name, password)
    return new_user

def save_account(user):
    '''
    A function that saves a user
    '''

    User.create_account(user)

def login(user_name, password):
    '''
    A function that checks if a user exists and returns a  boolean
    '''

    return User.user_exist(user_name, password)

def create_credentials(account, username, password):
    '''
    A function that creates new credentials
    '''
    new_credentials = Credentials(account, username, password)
    return new_credentials

def save_credentials(credentials):
    '''
    A function that saves credentials
    '''

    credentials.save_credentials()

def delete_credentials(credentials):
    '''
    A function that deletes credentials
    '''

    credentials.delete_credentials()

def find_credentials(account):
    '''
    A function that finds credentials by account and returns them
    '''

    return Credentials.find_by_account(account)

def check_existing_credentials(account):
    '''
    A function that checks if credentials exists with that account and returns a boolean
    '''

    return Credentials.credentials_exist(account)

def display_credentials():
    '''
    A function that returns saved credentials
    '''

    return Credentials.display_credentials()

def generate_password(psw_len):
    '''
    generate a new password
    Args:
    psw_len: preffered password length
    '''

    return "".join(secrets.choice(string.ascii_letters+string.digits) for i in range(psw_len))

def copy_credential(password):
    '''
    A function that allows copy and paste password to clipboard
    '''

    return Credentials.copy_password(password)

def main():
    print('Hello! Welcome to your Vault')
    logged_in = False

    while True:
        print("Do you want to sign up or login?")
        print("Click 's' to sign up or 'l' to login")
        answer = input()

        if answer == 'l':
            print('Enter your username: ')
            user_name = input()
            print('Enter your password: ')
            password = input()

            logged_in = login(user_name, password) if answer == 'l' else False
            

            while logged_in:
                print('\n')
                print('Use these short codes : \n sc - save an already existing account credentials \n cc - create a new credential \n vc - view your credentials \n fc - find credentials \n dl - delete credential \n copy - copy credentials \n ex - logout ')
                print('\n')

                short_code = input().lower()

                if short_code == 'cc':
                    print('Enter the name of the account you are creating')
                    account = input()

                    print('Enter the username: ')
                    username = input()

                    print('Password: ')
                    print('Would you like us to automatically generate you a password? y/n')
                    ps = input().lower()

                    if ps == 'y':
                        print('Enter your preferred password length')
                        ps_len = int(input())
                        password = generate_password(ps_len)
                        print(f'Your new password for {account} is {password}')

                    elif ps == 'n':
                        print('Create your password: ')
                        password = input()

                    else:
                        print('Invalid choice!')

                    save_credentials(create_credentials(account, username, password))

                    print(f'Account credentials for {account} has been saved, username: {username} password: {password}')
                    print('\n')
                elif short_code == 'sc':
                    print('save an existing Credentials Account')
                    print("-"*10)

                    print(' Account ...')
                    account = input()

                    print(f'\n username ...')
                    username = input()

                    print('\n password ...')
                    password = input()

                    save_credentials(create_credentials(account, username, password)) # create & save new credentials.
                    print('\n')
                    print(f'{account} username: {username} password: {password} created successfully')
                    print('-------------------------------------------------------------------------\n')
                elif short_code == 'vc':

                    if display_credentials():
                        print('Here is a list of all your credentials')
                        print('\n')

                        for credentials in display_credentials():
                            print(f'account: {credentials.account} username: {credentials.username} password: {credentials.password}')

                        print('\n')
                    else:
                        print('\n')
                        print('You dont seem to have any credentials saved yet')
                        print('\n')

                elif short_code == 'dl':

                    print('Enter the account you want to delete: ')
                    search_account = input()

                    if check_existing_credentials(search_account):
                        search_credentials = find_credentials(account)
                        print(f'username: {search_credentials.username} password: {search_credentials.password}')
                        print('-'* 40)
                        print(f"Do you want to delete {search_account} credentials? Click 'y' to delete or any other letter to skip")
                        answer = input().lower()
                        if answer == 'y':
                            delete_credentials(search_credentials)
                            print('Account Deleted')

                        else:
                            print('Skipped')

                    else:
                        print(f'{search_account} account Credentials do not exist')

                elif short_code == 'fc':

                    print('Enter the number you want to search for')

                    search_account = input()
                    if check_existing_credentials(search_account):
                        search_credentials = find_credentials(account)
                        print(f'username: {search_credentials.username} password: {search_credentials.password}')
                        print('-'* 20)

                    else:
                        print(f'{search_account} account Credentials does not exist')

                elif short_code == 'copy':

                    account = input('Enter the site account for the credential password to copy: ')
                    copy_credential(account)
                    print('Account removed')

                elif short_code == 'ex':
                    print(f'Goodbye...{user_name} ...')
                    break

                else:
                    print('I really didn\'t get that. Please use the short codes')
                    print('\n')

            else:
                print('Wrong username or password.Try again')
                print('\n')

        elif answer == 's':
            print("Create new account")

            print('Username: ')
            user_name = input()

            print('password: ')
            password = input()
    
            save_account(create_account(user_name, password))
            print(f'Account for {user_name} has been created')
            print("\n")

        else:
            print('Invalid Username')

    else:
        print('Invalid choice!!')

if __name__ == '__main__':

    main()
            
