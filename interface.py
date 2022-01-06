#!/usr/bin/env python3
from user import User

def function():
    pass

def create_new_user(account_name,user_name,password):
    new_account = User(account_name,user_name,password)
    return new_account

def save_account(User):
    User.save_user()

def display_account():
    return User.display_user()

def passwordLocker():
    print('use these short codes:\n 1- Create New Account:\n 2- Display Account')
    shortCode = input().lower().strip()
    if shortCode == '1':
        print('create New Account')
        print('-'*25)
        print('Enter your Account Name:')
        account_name=input().lower()
        print('Enter your Userame:')
        user_name=input().lower()
        print('Enter your password:')
        password=input()
        save_account(create_new_user(account_name, user_name, password))

    while True:
        print('use these short codes:\n 1-Create Account:\n 2-Display Account \n 3-Exit')
        shortCode = input().lower().strip()
        if shortCode == '1':
            print('create New Account')
            print('-'*30)
            print('User_name')
            user_name=input().lower()
            print('-'*30)
            print('Enter your password')
            password=input()
            save_account(create_new_user(account_name, user_name, password))
        elif shortCode == '2':
            for i in display_account():
                print('Your Account is:'+' '+ i.account_name + '\n' + 'Your Username is:'+' '+ i.user_name + '\n' + 'Your password is:'+' '+i.password)
        elif shortCode == '3':
            break

if __name__=='__main__':
    passwordLocker()
