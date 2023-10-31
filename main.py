class User:
    id = ''
    name = ''
    user_name = ''
    password = ''

    def __init__(self, Id, name, user_name, password):
        self.id = Id
        self.nanw = name
        self.user_name = user_name
        self.password = password

    def change_password(self, current_passord, new_password):
        if self.password == current_passord:
            self.password = new_password
            print('Successfully password change!')
        else:
            print('Current password is incorrect!')

        usr = User(1, 'michael', 'miba2', '123456')
        usr.change_password('123457', '1q2w4e')
        usr.change_password('126456', '1q2w3e')

