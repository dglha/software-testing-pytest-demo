import pytest
from configs.Config import TestData
from tests.test_base import BaseTest
from pages.WithDrawPage import WithdrawPage


@pytest.mark.order(5)
class TestWithdrawPage(BaseTest):

    """ TC031 """
    def test_withdraw(self):
        self.withdrawPage = WithdrawPage(self.driver)
        self.withdrawPage.do_login(TestData.USER_ID, TestData.PASSWORD)
        self.withdrawPage.do_withdraw(TestData.WITHDRAW_DATA)

        text = self.withdrawPage.get_alert_text()

        assert text != TestData.WITHDRAW_ACCOUNT_FAILURE_TEXT
