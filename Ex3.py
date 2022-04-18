from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"


chrome_service = Service("./chromedriver.exe")
chrome_option = Options()

chrome_option.add_argument("start-maximized")


# Get Driver
driver = webdriver.Chrome(service=chrome_service, options=chrome_option)


def test_page():
    driver.get("https://the-internet.herokuapp.com/login")
    try:
        username = driver.find_element(by=By.XPATH, value='//*[@id="username"]')
        password = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
        login_btn = driver.find_element(by=By.XPATH, value='//*[@id="login"]/button/i')
    except Exception as e:
        print(e)

    # Send keys
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    login_btn.click()

    # Navigate back
    driver.back()

    input_list = driver.find_elements(by=By.TAG_NAME, value="input")

    for input in input_list:
        print("Element: " + input.get_attribute("name"))

    driver.implicitly_wait(time_to_wait=30)

    return True


def get_elements_of_webpage(link: str):
    driver.get(link)
    try:
        print(
            "=================================================================================================="
        )
        print(driver.title + " - " + driver.current_url)
        input_list = driver.find_elements(by=By.TAG_NAME, value="input")

        for input in input_list:
            name = (
                 input.get_attribute("name")
                 if input.get_attribute("name")
                 else input.get_attribute("id")
            )
            value = (
                input.get_attribute("placeholder")
                if input.get_attribute("placeholder")
                else input.get_attribute("value")
            )
            print(f"Input element: {input.tag_name} - {name} - {value}")

        option_list = driver.find_elements(by=By.TAG_NAME, value="option")
        for option in option_list:
            print(f'Option element: {option.text} - {option.get_attribute("value")}')
        
    except Exception as e:
        print(e)


def main():
    get_elements_of_webpage("https://demoqa.com/automation-practice-form")
    get_elements_of_webpage("https://testpages.herokuapp.com/styled/basic-html-form-test.html")
    # get_elements_of_webpage("https://www.seleniumeasy.com/test/input-form-demo.html") # Error 404
    get_elements_of_webpage("https://formy-project.herokuapp.com/form")
    get_elements_of_webpage("https://www.saucedemo.com/")


    # Quit
    driver.quit()


if __name__ == "__main__":
    main()
