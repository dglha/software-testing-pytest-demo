from pages.LoginPage import LoginPage
from selenium.webdriver.common.by import By

class LogoutPage(LoginPage):
    LOGOUT_BUTTON = (By.XPATH, "/html/body/div[3]/div/ul/li[15]/a")

    def __init__(self, driver):
        super().__init__(driver)

    def is_logout_button_visible(self):
        return self.is_visible(self.LOGOUT_BUTTON)

    def do_logout(self):
        self.do_click(self.LOGOUT_BUTTON)

    def get_logout_alert_text(self):
        return self.get_alert_text()
