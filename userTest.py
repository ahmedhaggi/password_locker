from user import User
import unittest

class TestUser(unittest.TestCase):
    '''Test class for password locker'''
    def setUp(self):
        '''create Account object'''
        self.new_account=User('Ahmed','halista','12345')

        '''tearDown method that does clean up after each test case has run.'''

    def tearDown(self):
        User.account_list=[]

        '''test_init test case to test if the object is initialized properly'''

    def test_init(self):
        self.assertEqual(self.new_account.account_name,'Ahmed')
        self.assertEqual(self.new_account.user_name,'halista')
        self.assertEqual(self.new_account.password,'12345')

    '''Test_save_account test case to test if the account object is saved into the account list'''
    def test_save_user(self):
        self.new_account.save_user()
        self.assertEqual(len(User.account_list),1)

    '''test_save_multiple_account to check if we can save multiple account objects to our account_list'''
    def test_save_multiple_account(self):
        self.new_account.save_user()
        test_account=User('Ahmed','halista','12345')
        test_account.save_user()
        self.assertEqual(len(User.account_list),2)

    '''test to check if we can find an account by account_name and display information.'''
    def test_account_find(self):
        self.new_account.save_user()
        test_account=User('Ahmed','halista','12345')
        test_account.save_user()
        found_user=User.find_by_name('Ahmed')
        self.assertEqual(found_user.account_name,test_account.account_name)

    '''test to check if we can return a Boolean  if we cannot find the account.'''
    def test_account_exists(self):
        self.new_account.save_user()
        test_account=User('Ahmed','halista','12345')
        test_account.save_user()
        account_exists = User.account_exists('12345')
        self.assertTrue(account_exists)

    '''method that returns a list of all accounts saved'''
    def test_display_user(self):
        self.assertEqual(User.display_user(),User.account_list)

    '''test_delete_account to test if we can remove an account from our account list'''
    def test_delete_user(self):
        self.new_account.save_user()
        test_user=User('Ahmed','halista','12345')
        test_user.save_user()
        self.new_account.delete_user()
        self.assertEqual(len(User.account_list),1)


if __name__=='__main__':
    unittest.main()
