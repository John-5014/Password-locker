#!/usr/bin/env python3.6
import secrets
import string
import pyperclip
from user import User, Credentials


def create_user(fname, lname, password):
    '''
    Function to create a new user account
    '''
    new_user = User(fname, lname, password)
    return new_user


def save_user(user):
    '''
    function to save user
    '''
    User.save_user(user)


def verify_user(first_name, password):
    '''
    function that veifies the acount
    '''
    checking_user = Credentials.check_user(first_name, password)
    return checking_user


def generate_password():
    '''
    function that generates passwords automatically
    '''

    N = 12

    gen_password = ''.join(secrets.choice(
        string.ascii_lowercase + string.digits)for i in range(N))

    return gen_password


def create_credential(user_name,site_name,account_name,password):
    '''
    function that creates new credential
    '''

    new_credential = Credentials(user_name,site_name,account_name,password)
    return new_credential


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


def delete_credential(credential):

  '''
  function that deletes credential account
  '''

  credential.delete_credential()


def find_by_site_name(site_name):

  '''
  function that finds a credential by name
  '''

  
  return Credentials.find_by_site_name(site_name)



def main():
    print(' ')
    print('Hi! Welcome to Password-locker.')

    while True:
        print(' ')
        print("-"*30)
        print(
            'Use the guide codes to choose: \n ca-Create an Account \n li-Log In \n ex-Exit')
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
            save_user(create_user(first_name, last_name, password))
            print(" ")
            print(
                f'New Account Created for: {first_name} {last_name} with password: {password}')

        elif short_code == 'li':
            print("-"*30)
            print(' ')
            print('To  login,enter your account details: ')
            user_name = input('Enter your first name- ').strip()
            password = str(input('Enter your password - '))
            user_exists = verify_user(user_name, password)

            if user_exists == user_name:
                print(
                    f'Welcome {user_name}.Please choose an option to continue.')
                print(' ')

                while True:


                  print("-"*30)
                  print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n dl-Delete \n copy-Copy Password \n ex-Exit')
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

                      
                      while True:
                        print(' ')
                        print("-"*30)
                        print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
                        psw_choice = input('Enter an option: ').lower().strip()
                        print("-"*30)
                        if psw_choice == 'ep':
                            print(" ")
                            password = input('Enter your password: ').strip()
                            break
                        elif psw_choice == 'gp':
                            password = generate_password()
                            break
                        elif psw_choice == 'ex':
                            break
                        else:
                            print('Wrong option entered. Retry.')
                            

                      save_credential(create_credential(user_name,site_name,account_name,password))
                      print(' ')
                      print(
                          f'Credential created: Site Name:{site_name} - Account Name: {account_name} - Password:{password}')
                      print(' ')   

                  elif short_code == 'dc':
                      print(' ')
                      if display_credential(user_name):
                        print('Here is a list of all your credentials')
                        print(' ')
                        for credential in display_credential(user_name):
                          print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password{credential.password}')
                          print(' ')
                  elif short_code == 'copy':
                    print(' ')
                    chosen_site = input('Enter the site name for the credential password to copy: ')
                    copy_credentials(chosen_site)
                    print('')

                  elif short_code == 'dl':
                    print('Enter the name of site to be deleted')
                    delete_account = input()

                    if find_by_site_name(delete_account):
                      delete_credential(find_by_site_name(delete_account))
                    else:
                      print('Sorry account not matched')
                  else:
                    print('Wrong option entered. Retry')
        else:
          print("-"*30)
          print(' ')
          print('Sorry wrong option enetered. Retry')

                
                


        
    
        
        


if __name__ == '__main__':
    unittest: main()
