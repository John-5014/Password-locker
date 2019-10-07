


import unittest

'''
Importing the unittest module
'''

from user import  User,Credentials  

# import the user class


class TestUser(unittest.TestCase):

  '''
  Test class that defines the behaviour for the class
  '''

  def setUp(self):


    '''
    set up () to run before each test cases
    '''

    self.new_user = User("Kaiser","John","abcdedfghi")
    # create User object
  

  def tearDown(self):
    User.user_list = []
    '''
    tearDown() to clean up after each test has run
    '''

  def test_init(self):
    '''
    test init to test if object is initialized properly
    '''
    self.assertEqual(self.new_user.first_name,"Kaiser")
    self.assertEqual(self.new_user.last_name,"John")
    self.assertEqual(self.new_user.password,"abcdedfghi")
  def test_save_user(self):
    '''
    test_save_user test case to test if the user object is saved into
    the user list
    '''

    self.new_user.save_user()

    # save the new user
    self.assertEqual(len(User.user_list),1)


  # def test_save_multiple_user(self):

  #   '''
  #   to test whether we can save multiple users
  #   '''

  #   self.new_user.save_user()
  #   test_user = User("Nute","tuli","23456")
  #   test_user.save_user()
  #   self.assertEqual(len(User.user_list),2)


  # def test_delete_user(self):
  #   self.new_user.save_user()
  #   test_user = User("Nute","tuli","23456")
  #   test_user.save_user()
  #   self.new_user.delete_user()
  #   self.assertEqual(len(User.user_list),1)



class TestCredentials(unittest.TestCase):

  '''
  Test class that defines test cases for the credentials class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
  '''
  def test_check_user(self):
    '''
    function to check whether the login function  check_user works as expected
    '''

    self.new__user = User("njoki","john","pwd123456")
    self.new__user.save_user()
    user2 = User ("Guli","Thor","pwd123456")
    user2.save_user()
    for user in User.user_list:
      if user.first_name == user2.first_name and user.password ==user2.password:
        current_user = user.first_name
    return current_user

    self.assertEqual(current_user,Credentials.check_user(user2.password,user2.first_name))
  def setUp(self):
    '''
		Function to create an account's credentials before each test
		'''
    self.new_credential= Credentials('Rubi','Facebook','Rubitog','pwd12')
  def test__init__(self):
    '''
		Test to if check the initialization/creation of credential instances is properly done
		'''
    self.assertEqual(self.new_credential.user_name,'Rubi')
    self.assertEqual(self.new_credential.site_name,'Facebook')
    self.assertEqual(self.new_credential.account_name,"Rubitog")
    self.assertEqual
    (self.new_credential.password,'pwd12')
	

  def test_save_credentials(self):
    '''
		Test to check if the new credential info is saved into the credentials list
		'''
    self.new_credential.save_credentials()
    
    self.assertEqual(len(Credentials.credentials_list),1)
  

  def tearDown(self):
    '''
    Function to clear the credentials list after every test
    '''
    Credentials.credentials_list = []
    User.user_list = []

  def test_display_credentials(self):
    '''
    test to check if the display_credentials(),displays correct credentials
    '''
    self.new_credential.save_credentials()
    twitter = Credentials('Chris','Twitter',"will","pwd456")
    twitter.save_credentials()
    LinkedIn = Credentials('chris','LinkedIn','will','pwd5678')
    LinkedIn.save_credentials()
    self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

  def test_find_by_site_name(self):

    '''
    test to check if the find_site_name methode returns the correct credential
    '''
    self.new_credential.save_credentials()
    twitter = Credentials('Chris','Twitter','will','pwd456')
    twitter.save_credentials()
    credentials_exists = Credentials.find_by_site_name('Twitter')
    self.assertEqual(credentials_exists,twitter)


      




      
    




if __name__ == '__main__':
    unittest.main()