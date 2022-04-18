from pages.NewCustomerPage import NewCustomerPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class NewAccountPage(NewCustomerPage):

    NEW_ACCOUNT_URL = "https://demo.guru99.com/v4/manager/addAccount.php"
    NEW_ACCOUNT_CUSTOMER_ID = (
        By.XPATH,
        "/html/body/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input",
    )
    NEW_ACCOUNT_DEPOSIT = (
        By.XPATH,
        "/html/body/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input",
    )
    NEW_ACCOUNT_TYPE = "/html/body/table/tbody/tr/td/table/tbody/tr[3]/td[2]/select"

    NEW_ACCOUNT_SUBMIT_BUTTON = (
        By.XPATH,
        "/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]",
    )

    NEW_ACCOUNT_RESULT_TEXT = (By.XPATH, '//*[@id="account"]/tbody/tr[1]/td/p')

    def __init__(self, driver):
        super().__init__(driver)

    def do_add_new_account(self, customer_id, account_data):
        self.driver.get(self.NEW_ACCOUNT_URL)

        self.do_send_keys(self.NEW_ACCOUNT_CUSTOMER_ID, customer_id)
        select = Select(self.driver.find_element(By.XPATH, value=self.NEW_ACCOUNT_TYPE))
        select.select_by_visible_text("Savings")
        self.do_send_keys(self.NEW_ACCOUNT_DEPOSIT, account_data["deposit"])

        self.do_click(self.NEW_ACCOUNT_SUBMIT_BUTTON)

    def get_result_of_add_new_account(self):
        """
        Getting result from adding new account
        return: str
        """

        return self.get_element_text(self.NEW_ACCOUNT_RESULT_TEXT)
