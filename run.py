#!/usr/bin/env python3.6
import secrets 
import string 
import pyperclip
from user import User,Credentials

def create_user(fname,lname,password):
  '''
  Function to create a new user account
  '''
  new_user = User(fname,lname,password)
  return new_user

def save_user(user):
  '''
  function to save user
  '''
  User.save_user(user)

def verify_user(first_name,password):
  '''
  function that veifies the acount
  '''
  checking_user = Credentials.check_user(first_name,password)
  return checking_user

def generate_password():
  '''
  function that generates passwords automatically
  '''

  N = 12

  gen_password = ''.join(secrets.choice(string.ascii_lowercase + string.digits)for i in range(N))

  return gen_password

def create_credential(credential):
    '''
    function that creates new credential
    '''

    Credentials.save_credentials(credential)


def save_credential(credential):

  '''
  function to save a credential
  '''
  Credentials.save_credentials(credential)

def display_credential(user_name):
  '''
	Function to display credentials saved by a user
	'''

  return Credentials.display_credentials(user_name)


def copy_credentials(site_name):

  '''
  Function to copy a credentials details to the clipboard
  '''

  return Credentials.copy_credentials(site_name)






  








