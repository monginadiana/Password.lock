#!/usr/bin/env python3.8
from user import User
from account import Credentials
import random
import string

def new_person (username,password):
    '''
    This is a function that creates a new user
    '''
    new_user = User(username,password)
    return new_user

def save_new_person(user):
    '''
    Function to save the new person
    '''
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
    '''
    Function to create a new account
    '''
    new_account= Credentials(account_name,username,password)
    return new_account

def save_social_account(account):
    '''
    function to save a social account's credentials
    '''
    account.save_account()

def delete_social_account(account):
    '''
    function to delete a saved social accounts
    '''
    account.delete_account()  
def display_accounts():
        """
        test method that returns a list of all accounts created in our list"
        """
        return Credentials.display_accounts()
def create_password(length=6):

    '''
    function that generates a password for you
    '''
    characters = string.ascii_letters +string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))




