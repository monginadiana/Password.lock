#!/usr/bin/env python3.8
from user import User
from account import Credentials
import random
import string

def new_person (username,password):
    """
    This is a function that creates a new user
    """
    new_user = User(username,password)
    return new_user

def save_new_person(user):
    """
    Function to save the new person
    """
    user.save_user()
def delete_new_person(user):
    """
    A function that deletes the added user in the list.
    """
    user.delete_user()
def find_new_person(user):
    """
    A function that allows users to find a new person in the list.
    """
    user.find_username()

def create_new_account(account_name,username,password):
    """
    Function to create a new account
    """
    new_account= Credentials(account_name,username,password)
    return new_account

def save_social_account(account):
    """
    function to save a social account's credentials
    """
    account.save_account()

def delete_social_account(account):
   """
   function to delete a saved social accounts
   """
   account.delete_account()  
def display_accounts():
        """
        test method that returns a list of all accounts created in our list"
        """
        return Credentials.display_accounts()
def create_password(length=6):
    """
    A funtion that allows users to be able to generate new password
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))
def main():
    print("WELCOME TO PERSONAL PASSWORD LOCKER, I HOPE THIS IS HELPFUL")
    print("What is your name?")
    print('\n')
    user_name= input()
    print('\n')
    print(f"Hello {user_name}! the cheat codes below will be of assistance to you as you interact with the application")
    print('\n')

    while True:

        print('cc - Create a new password locker account')
        print('lg - Log in into your created account')
        print('ex - Exit your password locker account')
        print('\n')

        short_code = input().lower()

        if short_code == 'cc':
            print('Create your password locker account')
            print("-"*10)

            print('Create your Username...')
            username = input()

            print('Create your password...')
            password = input()

            save_new_person(new_person(username,password))

            print ('\n')
            print(f'Congratulations {username} you have succcessfully created your account!')

            print ('\n')
            print('You can now log in using the username and password created')

            print('Username...')
            login_username = input()

            print('Password...')
            login_password = input()
            if username != login_username or password != login_password:
                print('Invalid Username or password!')
                print('Please enter your password....')
                login_username = input()

                print('Please enter your password...')
                login_password = input()

            else :
                    print ('\n')
                    print(f'Hello {login_username}. Welcome to your password locker account!')
                    print ('\n')
                    social_account()
        elif short_code == 'lg':
             
                print('Log in to your existing account')
                print('Username....')
                lg_username = input()

                print('Password....')
                lg_password = input()

                if lg_username != 'Diana' and lg_password != '@Mongina':
                    print('The account does not exist, please create an account')
                else:
                    print(f'Hello {lg_username}. This is your password locker account, Welcome!')
                    print ('\n')
                    social_account()
        elif short_code == 'ex':

                print('Bye! Come back soon !')
                break
        else:
                print('Wrong short code! Try again')


def social_account():
    print('Now you can store your social accounts credentials here!')
  
    print('Use these short codes to navigate through')
    print ('\n')

if __name__ == '__main__':

    main()



