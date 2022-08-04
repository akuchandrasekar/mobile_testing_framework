from tests.base_tests import BaseTests
from settings import TEST_DATA


class TestLoginTwo(BaseTests):

    def test_login_two(self, init):
        # Fetch Data from YAML file and use it in test cases instead of hard coding
        self.login_actions.login_steps(email=TEST_DATA['login']['email'], password=TEST_DATA['login']['password'])
        assert self.my_site.get_text_my_site_title() == "yourblogname"
