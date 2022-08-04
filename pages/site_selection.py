from pages.my_site import *


class SiteSelection(MySite):
    if platform == 'ios':
        final_done_button = ('accessibility_id', 'Done')
    else:
        final_done_button = ('id', 'primary_button')

    def click_final_done_button(self):
        self.click(self.final_done_button)