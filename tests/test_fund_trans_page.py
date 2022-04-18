import pytest
from configs.Config import TestData
from tests.test_base import BaseTest
from pages.FundTransferPage import FundTransferPage


@pytest.mark.order(6)
class TestFundTransferPage(BaseTest):

    """ TC040 """
    def test_fund_trans(self):
        self.fundTransPage = FundTransferPage(self.driver)
        self.fundTransPage.do_login(TestData.USER_ID, TestData.PASSWORD)
        self.fundTransPage.do_fund_trans(TestData.FUND_TRANS_DATA)

        text = self.fundTransPage.get_alert_text()

        assert "does not exist!!!" not in text
