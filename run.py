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




def main():
  print(' ')
  print('Hi! Welcome to Password-locker.')

  while True:
    print(' ')
    print("-"*30)
    print('Use the guide codes to choose: \n ca-Create an Account \n li-Log In \n ex-Exit')
    short_code = input('Enter a choice: ').lower().strip()
    if short_code == 'ex':
      break

    elif short_code == 'ca':
      print("-"*30)
      print(' ')
      print('To create a new account:')

      first_name = input('Enter your first name- \n').strip()
      last_name = input('Enter your last name- \n').strip()

      password = input('Enter your password \n').strip()
      save_user(create_user(first_name,last_name,password))
      print(" ")
      print(f'New Account Created for: {first_name} {last_name} with password: {password}')


    elif short_code == 'li':
      print("-"*30)
      print(' ')
      print('To  login,enter your account details: ')
      user_name = input('Enter your first name- ').strip()
      password = str(input('Enter your password - '))
      user_exists = verify_user(user_name,password)

      if user_exists == user_name:
        print(f'Welcome {user_name}.Please choose an option to continue.')
        print(' ')

  while True:
    print("-"*30)
    print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n ex-Exit')
    short_code = input('Enter a choice: ').lower().strip()
    print("-"*30)
    if short_code == 'ex':
      print(" ")
      print(f'Goodbye {user_name}')
      break
    elif short_code == 'cc':
      print(' ')
      print('Enter your credential details:')
      site_name = input('Enter the site\'s name-').strip()
      account_name = input('Enter your account\'s name-').strip()


    









if __name__ == '__main__':
  unittest:main()






  








