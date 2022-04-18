import pytest
from configs.Config import TestData
from tests.test_base import BaseTest
from pages.LogoutPage import LogoutPage


@pytest.mark.order(8)
class TestLogoutPage(BaseTest):

    """ TC064 """
    def test_logout(self):
        self.logoutPage = LogoutPage(self.driver)
        self.logoutPage.do_login(TestData.USER_ID, TestData.PASSWORD)

        if self.logoutPage.is_logout_button_visible():
            self.logoutPage.do_logout()

        text = self.logoutPage.get_alert_text()

        assert (
            text == TestData.LOGOUT_SUCCESS_TEXT
        ), "Test failure - Account does not exist"
