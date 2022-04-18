from pages.LoginPage import LoginPage
from selenium.webdriver.common.by import By


class NewCustomerPage(LoginPage):

    NEW_CUSTOMER_BUTTON = (By.XPATH, "/html/body/div[3]/div/ul/li[2]/a")
    NEW_CUSTOMER_URL = "https://demo.guru99.com/v4/manager/addcustomerpage.php"

    CUSTOMER_NAME = (
        By.XPATH,
        "/html/body/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input",
    )
    GENDER_MALE = (
        By.XPATH,
        "/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]",
    )
    DATE_OF_BIRTH = (By.ID, "dob")
    ADDRESS = (
        By.XPATH,
        "/html/body/table/tbody/tr/td/table/tbody/tr[7]/td[2]/textarea",
    )
    CITY = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[8]/td[2]/input")
    STATE = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[9]/td[2]/input")
    PIN = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[10]/td[2]/input")
    MOBILE_NUMBER = (
        By.XPATH,
        "/html/body/table/tbody/tr/td/table/tbody/tr[11]/td[2]/input",
    )
    EMAIL = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[12]/td[2]/input")
    CUSTOMER_PASSWORD = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[13]/td[2]/input")
    SUBMIT_BUTTON = (
        By.XPATH,
        "/html/body/table/tbody/tr/td/table/tbody/tr[14]/td[2]/input[1]",
    )

    CUSTOMER_ID_RESULT = (By.XPATH, '//*[@id="customer"]/tbody/tr[4]/td[2]')
    CUSTOMER_REG_RESULT = (
        By.XPATH,
        "/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p",
    )
    CUSTOMER_EMAIL_RESULT = (By.XPATH, '//*[@id="customer"]/tbody/tr[13]/td[2]')

    # Delete customer info
    DELETE_CUSTOMER_URL = "https://demo.guru99.com/v4/manager/DeleteCustomerInput.php"
    DETELE_CUSTOMER_ID_INPUT = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input")
    DELETE_CUSTOMER_SUBMIT = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[7]/td[2]/input[1]")


    def __init__(self, driver):
        super().__init__(driver)

    def is_submit_button_visible(self):
        return self.is_visible(self.SUBMIT_BUTTON)

    def do_add_customer(self, customer_data: dict):
        self.driver.get(self.NEW_CUSTOMER_URL)
        self.do_send_keys(self.CUSTOMER_NAME, customer_data["customer_name"])
        self.do_click(self.GENDER_MALE)
        self.do_send_keys(self.DATE_OF_BIRTH, customer_data["date_of_birth"])
        self.do_send_keys(self.ADDRESS, customer_data["address"])
        self.do_send_keys(self.CITY, customer_data["city"])
        self.do_send_keys(self.STATE, customer_data["state"])
        self.do_send_keys(self.PIN, customer_data["pin"])
        self.do_send_keys(self.MOBILE_NUMBER, customer_data["mobile_number"])
        self.do_send_keys(self.EMAIL, customer_data["email"])
        self.do_send_keys(self.CUSTOMER_PASSWORD, customer_data["password"])

        self.do_click(self.SUBMIT_BUTTON)

    def get_result_of_add_new_customer(self):
        """
        Return result of add new customer
        return: (id, email, reg_result_text: bool)
        """
        customer_id = self.get_element_text(self.CUSTOMER_ID_RESULT)
        customer_email = self.get_element_text(self.CUSTOMER_EMAIL_RESULT)
        result_text = self.get_element_text(self.CUSTOMER_REG_RESULT)

        return (customer_id, customer_email, result_text)

    def delete_customer(self, customer_id):
        """
            Delete customer with id
            return: bool
        """
        self.driver.get(self.DELETE_CUSTOMER_URL)
        self.do_send_keys(self.DETELE_CUSTOMER_ID_INPUT, customer_id)
        self.do_click(self.DELETE_CUSTOMER_SUBMIT)

        self.do_alert_accept()
        text = self.get_alert_text()
        return text == "Customer does not exist!!"
