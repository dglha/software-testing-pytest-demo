import pytest
from configs.Config import TestData
from tests.test_base import BaseTest
from pages.LoginPage import LoginPage


@pytest.mark.order(1)
class TestLoginPage(BaseTest):
    def test_login_button_visible(self):
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.is_login_button_visible()

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    """ TC001 """
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_ID, TestData.PASSWORD)

        text = self.loginPage.get_element_text(self.loginPage.SUCESS_TEXT)

        assert text == TestData.LOGIN_PAGE_SUCCESS_TEXT
