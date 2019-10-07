#!/usr/bin/env python3.6

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






  








