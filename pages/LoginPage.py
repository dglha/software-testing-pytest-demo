from configs.Config import TestData
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USER_ID = (By.XPATH, "/html/body/form/table/tbody/tr[1]/td[2]/input")
    PASSWORD = (By.XPATH, "/html/body/form/table/tbody/tr[2]/td[2]/input")
    LOGIN_BUTTON = (By.XPATH, "/html/body/form/table/tbody/tr[3]/td[2]/input[1]")

    SUCESS_TEXT = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[3]/td")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.LOGIN_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_login_button_visible(self):
        return self.is_visible(self.LOGIN_BUTTON)

    def do_login(self, user_id, password):
        self.do_send_keys(self.USER_ID, user_id)
        self.do_send_keys(self.PASSWORD, password)

        self.do_click(self.LOGIN_BUTTON)
