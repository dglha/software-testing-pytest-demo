import pytest
from configs.Config import TestData
from tests.test_base import BaseTest
from pages.NewCustomerPage import NewCustomerPage


@pytest.mark.order(2)
class TestNewCustomerPage(BaseTest):

    """ TC009 """
    def test_add_customer(self):
        self.newCustomerPage = NewCustomerPage(self.driver)
        self.newCustomerPage.do_login(TestData.USER_ID, TestData.PASSWORD)

        self.newCustomerPage.do_add_customer(TestData.CUSTOMER_DATA)
        (
            customer_id,
            customer_email,
            result_text,
        ) = self.newCustomerPage.get_result_of_add_new_customer()

        self.newCustomerPage.delete_customer(customer_id)

        assert customer_email == TestData.CUSTOMER_DATA["email"], "Email mismatch!!!"
