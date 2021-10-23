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
def

