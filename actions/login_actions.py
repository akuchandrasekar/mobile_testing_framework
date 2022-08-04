from actions.base_screen_action import BaseScreenAction
from pages.email_form import EmailForm
from pages.my_site import MySite
from pages.password_form import PasswordForm
from pages.password_type import PasswordType
from pages.signup_wall import SignupWall
from pages.site_selection import SiteSelection


class LoginActions(BaseScreenAction):

    def __init__(self, driver):
        self.driver = driver
        self.email_form = EmailForm(driver)
        self.my_site = MySite(driver)
        self.password_form = PasswordForm(driver)
        self.password_type = PasswordType(driver)
        self.signup_wall = SignupWall(driver)
        self.site_selection = SiteSelection(driver)

    def login_steps(self, email, password):
        self.signup_wall.click_login_button()
        self.signup_wall.click_login_with_email_button()
        self.email_form.input_email(email)
        self.email_form.click_email_done_button()
        self.password_type.click_login_enter_password_button()
        self.password_form.input_password(password)
        self.password_form.click_password_done_button()
        self.site_selection.click_final_done_button()

# 1. Click on Login and Choose continue with WordPress
# 2. Enter Email and Click Done
# 3. Choose Enter your password instead option
# 4. Enter Password and Click Done
# 5. Click on Done