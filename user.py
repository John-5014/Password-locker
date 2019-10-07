import pyperclip

import string

# Global Variables
global users_list 
class User:

  user_list = []

  def __init__(self, first_name,last_name, password):

    self.first_name = first_name
    self.last_name = last_name
    self.password = password

  def save_user(self):
    User.user_list.append(self)
    

  # def delete_user(self):
  #   '''
  #   deletes a saved user account from the list
  #   '''

  #   User.user_list.remove(self)


class Credentials:
  '''
  create class Credentials ,generates passwords and save information
  '''

  credentials_list=[]
  user_credentials_list = []
  @classmethod
  def check_user(cls,first_name,password):
    '''
    Method that checks if the name and password entered match entries in the users_list
    '''

    current_user = ''
    for user in User.user_list:
      if (user.first_name == first_name and user.password == password):
        current_user = user.first_name
    return current_user





  def __init__(self,user_name,site_name,account_name,password):

      # create instance variables
    self.user_name = user_name
    self.site_name = site_name
    self.account_name = account_name
    self.password = password
  

  def save_credentials(self):

  # global users_list

    Credentials.credentials_list.append(self)






  @classmethod
  def find_by_site_name(cls,site_name):
    '''
		Method that takes in a site_name and returns a credential that matches that site_name.
		'''
    for credentials in cls.credentials_list:
    
      if credentials.site_name == site_name:
        return credentials


  @classmethod
  def delete_credential(self):

    Credentials.credentials_list.remove(self)



    
  @classmethod
  def display_credentials(cls,user_name):
    return cls.credentials_list




  @classmethod
  def copy_credentials(cls,site_name):

    find_credential = Credentials.find_by_site_name(site_name)
    return pyperclip.copy(find_credential.password)

      