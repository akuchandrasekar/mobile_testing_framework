from tests.base_tests import BaseTests
from settings import TEST_DATA


class TestLogin(BaseTests):

    def test_login(self, init):
        self.login_actions.login_steps(email='yourblog@email.com', password='yourblogpassword')
        assert self.my_site.get_text_my_site_title() == "yourblogname"
