from infra.base import Base
from settings import *


class MySite(Base):
    if platform == 'ios':
        my_site_title = ('xpath', '(//XCUIElementTypeStaticText[@name="yourblogname"])[1]')
        posts_icon = ('accessibility_id', 'Posts')
    else:
        my_site_title = ('id', 'my_site_title_label')
        posts_icon = ('id', 'quick_action_posts_button')

    def get_text_my_site_title(self):
        return self.get_text(self.my_site_title)

    def click_posts_icon(self):
        self.click(self.posts_icon)