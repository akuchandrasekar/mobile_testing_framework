from pages.my_site import *


class PasswordForm(MySite):
    if platform == 'ios':
        password_input = ('accessibility_id', 'Password')
        password_done_button = ('accessibility_id', 'Next')
    else:
        password_input = ('id', 'input')
        password_done_button = ('id', 'primary_button')

    def input_password(self, password):
        self.send_keys(self.password_input, password)

    def click_password_done_button(self):
        self.click(self.password_done_button)