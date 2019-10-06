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


  def test_save_multiple_contact(self):

    '''
    to test whether we can save multiple users
    '''

    self.new_user.save_user()
    test_user = User("Nute","tuli","23456")
    test_user.save_user()
    self.assertEqual(len(User.user_list),2)


if __name__ == '__main__':
    unittest.main()