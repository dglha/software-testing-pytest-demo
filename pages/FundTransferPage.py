from .LoginPage import LoginPage
from selenium.webdriver.common.by import By


class FundTransferPage(LoginPage):
    FUND_TRANSFER_ACCOUNT_PAYER_ID = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input")
    FUND_TRANSFER_ACCOUNT_PAYEE_ID = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input")
    FUND_TRANSFER_ACCOUNT_AMOUNT = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[6]/td[2]/input")
    FUND_TRANSFER_ACCOUNT_DESCRIPTION = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[7]/td[2]/input")
    FUND_TRANSFER_ACCOUNT_SUBMIT_BUTTON = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[8]/td[2]/input[1]")
    FUND_TRANSFER_ACCOUNT_URL = "https://demo.guru99.com/v4/manager/FundTransInput.php"

    def __init__(self, driver):
        super().__init__(driver)

    def is_fund_submit_button_visible(self):
        return self.is_visible(self.FUND_TRANSFER_ACCOUNT_SUBMIT_BUTTON)

    def do_fund_trans(self, fund_trans_data: dict):
        self.driver.get(self.FUND_TRANSFER_ACCOUNT_URL)

        self.do_send_keys(self.FUND_TRANSFER_ACCOUNT_PAYER_ID, fund_trans_data["account_payer_id"])
        self.do_send_keys(self.FUND_TRANSFER_ACCOUNT_PAYEE_ID, fund_trans_data["account_payee_id"])
        self.do_send_keys(self.FUND_TRANSFER_ACCOUNT_AMOUNT, fund_trans_data["amount"])
        self.do_send_keys(self.FUND_TRANSFER_ACCOUNT_DESCRIPTION, fund_trans_data["description"])

        self.do_click(self.FUND_TRANSFER_ACCOUNT_SUBMIT_BUTTON)

