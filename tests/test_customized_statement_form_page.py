import pytest
from configs.Config import TestData
from tests.test_base import BaseTest
from pages.CustomisedStatementPage import CustomisedStatementPage


@pytest.mark.order(7)
class TestCustomizedStatmentPage(BaseTest):

    """ TC051 """
    def test_fund_trans(self):
        self.cusStatementPage = CustomisedStatementPage(self.driver)
        self.cusStatementPage.do_login(TestData.USER_ID, TestData.PASSWORD)
        self.cusStatementPage.do_cus_statement_form(TestData.CUS_STATEMENT_DATA)

        text = self.cusStatementPage.get_alert_text()

        assert text != TestData.CUS_STATEMENT_FAILURE_TEXT
