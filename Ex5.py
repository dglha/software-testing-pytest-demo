import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

URL = "http://www.zx-test.xyz/dynamic-data-loading-demo.html"  # old site not working!!!


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
    # driver.close()


@pytest.mark.usefixtures("setup")
class TestFetchUser:
    # def test_get_data(self):
    #     wait = WebDriverWait(
    #         driver=self.driver,
    #         poll_frequency=2,
    #         ignored_exceptions=[
    #             ElementNotVisibleException,
    #             ElementNotSelectableException,
    #         ],
    #         timeout=10,
    #     )

    #     get_user_btn = self.driver.find_element(by=By.XPATH, value='//*[@id="save"]')
    #     get_user_btn.click()

    #     docs = wait.until(
    #         EC.presence_of_element_located((By.XPATH, '//*[@id="loading"]/br[1]'))
    #     )

    #     text = self.driver.find_element(by=By.XPATH, value='//*[@id="loading"]').text

    #     assert "loading..." not in text

    def test_get_firstname(self):
        wait = WebDriverWait(
            driver=self.driver,
            poll_frequency=2,
            ignored_exceptions=[
                ElementNotVisibleException,
                ElementNotSelectableException,
            ],
            timeout=10,
        )

        get_user_btn = self.driver.find_element(by=By.XPATH, value='//*[@id="save"]')
        get_user_btn.click()

        docs = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loading"]/br[1]'))
        )

        text = self.driver.find_element(by=By.XPATH, value='//*[@id="loading"]').text

        assert "First Name" in text
