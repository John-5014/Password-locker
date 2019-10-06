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
  

  # def tearDown(self):
  #   User.user_list = []

  def test_init(self):
    '''
    test init to test if object is initialized properly
    '''
    self.assertEqual(self.new_user.first_name,"Kaiser")
    self.assertEqual(self.new_user.last_name,"John")
    self.assertEqual(self.new_user.password,"abcdedfghi")

if __name__ == '__main__':
    unittest.main()