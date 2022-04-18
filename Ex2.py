from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


chrome_service = Service("./chromedriver.exe")
chrome_option = Options()

chrome_option.add_argument("start-maximized")

driver = webdriver.Chrome(service=chrome_service, options=chrome_option)
driver.get("https://the-internet.herokuapp.com")

# Set new size
driver.set_window_size(375, 812)

# Wait 10s
driver.implicitly_wait(10)
driver.quit()


print(driver.title)