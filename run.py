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


