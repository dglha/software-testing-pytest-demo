import pytest
from configs.Config import TestData
from tests.test_base import BaseTest
from pages.DepositPage import DepositPage


@pytest.mark.order(4)
class TestDepositPage(BaseTest):

    """ TC022 """
    def test_deposit(self):
        self.depositPage = DepositPage(self.driver)
        self.depositPage.do_login(TestData.USER_ID, TestData.PASSWORD)
        self.depositPage.do_deposit(TestData.DEPOSIT_DATA)

        text = self.depositPage.get_alert_text()

        assert text != TestData.DEPOSIT_ACCOUNT_FAILURE_TEXT
