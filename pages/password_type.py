from pages.my_site import *


class PasswordType(MySite):
    if platform == 'ios':
        login_enter_password_button = ('accessibility_id', 'Enter your password instead.')
    else:
        login_enter_password_button = ('id', 'login_enter_password')

    def click_login_enter_password_button(self):
        self.click(self.login_enter_password_button)