from .LoginPage import LoginPage
from selenium.webdriver.common.by import By


class WithdrawPage(LoginPage):
    WITHDRAW_ACCOUNT_ID = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[6]/td[2]/input")
    WITHDRAW_ACCOUNT_AMOUNT = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[7]/td[2]/input")
    WITHDRAW_ACCOUNT_DESCRIPTION = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[8]/td[2]/input")
    WITHDRAW_ACCOUNT_SUBMIT_BUTTON = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[12]/td[2]/input[1]")
    WITHDRAW_ACCOUNT_URL = "https://demo.guru99.com/v4/manager/WithdrawalInput.php"

    def __init__(self, driver):
        super().__init__(driver)

    def is_withdraw_submit_button_visible(self):
        return self.is_visible(self.WITHDRAW_ACCOUNT_SUBMIT_BUTTON)

    def do_withdraw(self, withdraw_data: dict):
        self.driver.get(self.WITHDRAW_ACCOUNT_URL)

        self.do_send_keys(self.WITHDRAW_ACCOUNT_ID, withdraw_data["account_id"])
        self.do_send_keys(self.WITHDRAW_ACCOUNT_AMOUNT, withdraw_data["amount"])
        self.do_send_keys(self.WITHDRAW_ACCOUNT_DESCRIPTION, withdraw_data["description"])

        self.do_click(self.WITHDRAW_ACCOUNT_SUBMIT_BUTTON)

