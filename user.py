class User:
    '''class that New intances of user'''
    account_list=[]
    def __init__(self,account_name,user_name,password):
        '''__init__ method helps to properties of our
        object'''
        self.account_name=account_name
        self.user_name=user_name
        self.password=password

    def save_user(self):
        '''a method save a new user'''
        User.account_list.append(self)

    def delete_user(self):
        User.account_list.remove(self)


    @classmethod
    def display_user(cls):
        return cls.account_list

    @classmethod
    def find_by_name(cls,name):
        for account in cls.account_list:
            if account.account_name == name:
                return account

    @classmethod
    def account_exists(cls,name):
        for account in cls.account_list:
            if account.password == name:
                return account
        return False
