from pages.my_site import *


class EmailForm(MySite):
    if platform == 'ios':
        email_input = ('accessibility_id', 'Login Email Address')
        email_done_button = ('accessibility_id', 'Login Email Next Button')
    else:
        email_input = ('id', 'input')
        email_done_button = ('id', 'primary_button')

    def input_email(self, email):
        self.send_keys(self.email_input, email)

    def click_email_done_button(self):
        self.click(self.email_done_button)