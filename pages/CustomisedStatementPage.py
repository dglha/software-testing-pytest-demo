from .LoginPage import LoginPage
from selenium.webdriver.common.by import By


class CustomisedStatementPage(LoginPage):
    CUS_STATEMENT_ACCOUNT_ID = (
        By.XPATH,
        "/html/body/table/tbody/tr/td/table/tbody/tr[6]/td[2]/input",
    )
    CUS_STATEMENT_ACCOUNT_FROM_DATE = (
        By.XPATH,
        "/html/body/table/tbody/tr/td/table/tbody/tr[7]/td[2]/input",
    )
    CUS_STATEMENT_ACCOUNT_TO_DATE = (
        By.XPATH,
        "/html/body/table/tbody/tr/td/table/tbody/tr[8]/td[2]/input",
    )
    CUS_STATEMENT_ACCOUNT_MINIMUM_TRANS = (
        By.XPATH,
        "/html/body/table/tbody/tr/td/table/tbody/tr[9]/td[2]/input",
    )
    CUS_STATEMENT_ACCOUNT_NUMBER_OF_TRANS = (
        By.XPATH,
        "/html/body/table/tbody/tr/td/table/tbody/tr[10]/td[2]/input",
    )
    CUS_STATEMENT_ACCOUNT_SUBMIT_BUTTON = (
        By.XPATH,
        "/html/body/table/tbody/tr/td/table/tbody/tr[13]/td[2]/input[1]",
    )
    CUS_STATEMENT_ACCOUNT_URL = (
        "https://demo.guru99.com/v4/manager/CustomisedStatementInput.php"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def is_submit_button_visible(self):
        return self.is_visible(self.CUS_STATEMENT_ACCOUNT_SUBMIT_BUTTON)

    def do_cus_statement_form(self, cus_statement_data: dict):
        self.driver.get(self.CUS_STATEMENT_ACCOUNT_URL)

        self.do_send_keys(
            self.CUS_STATEMENT_ACCOUNT_ID, cus_statement_data["account_id"]
        )
        self.do_send_keys(
            self.CUS_STATEMENT_ACCOUNT_FROM_DATE, cus_statement_data["from_date"]
        )
        self.do_send_keys(
            self.CUS_STATEMENT_ACCOUNT_TO_DATE, cus_statement_data["to_date"]
        )
        self.do_send_keys(
            self.CUS_STATEMENT_ACCOUNT_MINIMUM_TRANS,
            cus_statement_data["minimum_trans_value"],
        )
        self.do_send_keys(
            self.CUS_STATEMENT_ACCOUNT_NUMBER_OF_TRANS,
            cus_statement_data["num_of_trans"],
        )

        self.do_click(self.CUS_STATEMENT_ACCOUNT_SUBMIT_BUTTON)
