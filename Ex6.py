import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.alert import Alert

URL = "http://www.zx-test.xyz/javascript-alert-box-demo.html"  # old site not working!!!


@pytest.fixture()
def setup(request):
    print("Initiating chrome driver")
    chrome_service = Service("./chromedriver.exe")
    chrome_option = Options()

    chrome_option.add_argument("start-maximized")
    # Get Driver
    driver = webdriver.Chrome(service=chrome_service, options=chrome_option)
    request.instance.driver = driver
    driver.get(URL)

    yield driver
    driver.close()


@pytest.mark.usefixtures("setup")
class TestJavaScriptAlertBox:
    def click_js_btn(self):
        btn = self.driver.find_element(by=By.XPATH, value = '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/button')
        btn.click()
    
    def accept_js_alert(self):
        self.alert = self.driver.switch_to.alert

    def test_js_alert(self):
        self.click_js_btn()
        self.accept_js_alert()

        self.alert.accept()


@pytest.mark.usefixtures("setup")
class TestJavaScriptConfirmBox:
    def click_js_btn(self):
        btn = self.driver.find_element(by=By.XPATH, value = '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button')
        btn.click()
    
    def accept_js_alert(self):
        self.alert = self.driver.switch_to.alert

    def test_js_confirm(self):
        self.click_js_btn()
        self.accept_js_alert()
        self.alert.accept()

        self.click_js_btn()
        self.alert.dismiss()

@pytest.mark.usefixtures("setup")
class TestJavaScriptPromptBox:
    def click_js_btn(self):
        btn = self.driver.find_element(by=By.XPATH, value = '//*[@id="easycont"]/div/div[2]/div[3]/div[2]/button')
        btn.click()
    
    def accept_js_alert(self):
        self.alert = self.driver.switch_to.alert

    def test_js_confirm(self):
        self.click_js_btn()
        self.accept_js_alert()
        self.alert.send_keys("Kiem thu phan mem 123")
        self.alert.accept()

        text = self.driver.find_element(by=By.XPATH, value='//*[@id="prompt-demo"]').text
        assert "Kiem thu phan mem 123" in text


# 

