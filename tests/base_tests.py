import pytest
from pages.my_site import MySite
from actions.login_actions import LoginActions


@pytest.mark.usefixtures('setup')
class BaseTests:

    @pytest.fixture
    def init(self):
        driver = self.driver
        self.my_site = MySite(driver)
        self.login_actions = LoginActions(driver)
