from pages.my_site import *


class SignupWall(MySite):
    if platform == 'ios':
        login_button = ('accessibility_id', 'Prologue Log In Button')
        login_with_email_button = ('accessibility_id', 'Log in with Email Button')
    else:
        login_button = ('id', 'login_button')

    def click_login_button(self):
        self.click(self.login_button)

    def click_login_with_email_button(self):
        if platform == 'ios':
            self.click(self.login_with_email_button)