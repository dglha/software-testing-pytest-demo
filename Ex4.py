from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

URL = "http://www.zx-test.xyz/dynamic-data-loading-demo.html"  # old site not working!!!

chrome_service = Service("./chromedriver.exe")
chrome_option = Options()

chrome_option.add_argument("start-maximized")


# Get Driver
driver = webdriver.Chrome(service=chrome_service, options=chrome_option)


def fetch_new_user():
    if not (driver.current_url == URL):
        driver.get(URL)

    get_user_btn = driver.find_element(by=By.XPATH, value='//*[@id="save"]')

    wait = WebDriverWait(
        driver=driver,
        poll_frequency=2,
        ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException],
        timeout=10
    )

    for i in range(1, 11):
        get_user_btn.click()

        docs = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loading"]/br[1]'))
        )


        unparse_text = driver.find_element(by=By.XPATH, value='//*[@id="loading"]').text

        parsed_text = unparse_text.replace("\n\n", " - ")

        image = driver.find_element(by=By.XPATH, value='//*[@id="loading"]/img')



        print(
            f'Fetched new user [{i}]: {parsed_text} - Image: {image.get_attribute("src")}'
        )


def main():
    fetch_new_user()
    driver.quit()


if __name__ == "__main__":
    main()
