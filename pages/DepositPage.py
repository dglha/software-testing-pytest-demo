from .LoginPage import LoginPage
from selenium.webdriver.common.by import By


class DepositPage(LoginPage):
    DEPOSIT_ACCOUNT_ID = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[6]/td[2]/input")
    DEPOSIT_ACCOUNT_AMOUNT = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[7]/td[2]/input")
    DEPOSIT_ACCOUNT_DESCRIPTION = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[8]/td[2]/input")
    DEPOSIT_ACCOUNT_SUBMIT_BUTTON = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[12]/td[2]/input[1]")
    DEPOSIT_ACCOUNT_URL = "https://demo.guru99.com/v4/manager/DepositInput.php"

    def __init__(self, driver):
        super().__init__(driver)

    def is_deposit_submit_button_visible(self):
        return self.is_visible(self.DEPOSIT_ACCOUNT_SUBMIT_BUTTON)

    def do_deposit(self, deposit_data: dict):
        self.driver.get(self.DEPOSIT_ACCOUNT_URL)

        self.do_send_keys(self.DEPOSIT_ACCOUNT_ID, deposit_data["account_id"])
        self.do_send_keys(self.DEPOSIT_ACCOUNT_AMOUNT, deposit_data["amount"])
        self.do_send_keys(self.DEPOSIT_ACCOUNT_DESCRIPTION, deposit_data["description"])

        self.do_click(self.DEPOSIT_ACCOUNT_SUBMIT_BUTTON)

