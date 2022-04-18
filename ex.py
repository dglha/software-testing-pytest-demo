from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

LINK = "https://demo.openmrs.org/openmrs//appointmentschedulingui/requestAppointment.page?patientId=1631fcd2-82ef-44dd-8ccb-33bde78d5d29&returnUrl=%2Fopenmrs%2Fcoreapps%2Fclinicianfacing%2Fpatient.page%3FpatientId%3D512%26"
BASE_LINK = "https://demo.openmrs.org/openmrs/login.htm"

USERNAME_INPUT = (By.ID, "username")
PASSWORD_INPUT = (By.ID, "password")
LOCATION_INPUT = (By.ID, "Inpatient Ward")
LOGIN_BTN = (By.ID, "loginButton")

APPOINTMENT_TYPE = (By.ID, "appointment-type")
DROPDOWN_TEST = (By.XPATH, "/html/body/div/div[3]/div[4]/form/p[1]/ul")
DROPDOWN_ITEM = (By.CSS_SELECTOR, ".ng-scope.ng-binding")


chrome_service = Service("./chromedriver.exe")
chrome_option = Options()

chrome_option.add_argument("start-maximized")


def do_click(by_locator):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(by_locator)
    ).click()


def do_send_keys(by_locator, text):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(by_locator)
    ).send_keys(text)


driver = webdriver.Chrome(service=chrome_service, options=chrome_option)
driver.get(BASE_LINK)

do_send_keys(USERNAME_INPUT, "Admin")
do_send_keys(PASSWORD_INPUT, "Admin123")
do_click(LOCATION_INPUT)
do_click(LOGIN_BTN)


driver.get(LINK)

do_send_keys(APPOINTMENT_TYPE, "a")
items = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(DROPDOWN_ITEM))
for item in items:
    if "Mental Health" == item.text:
        item.click()
    

sleep(10)

driver.quit()


print(driver.title)
