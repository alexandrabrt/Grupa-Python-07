from handlers.database import get_user_list, create_user

if __name__ == '__main__':
    # create_user('Donald', 'Duck', 'donald.duck@disney.com')

    user_list = get_user_list()
    for user in user_list:
        print(user.id, user)