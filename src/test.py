from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from drivers.driver_factory import create_driver


driver = create_driver()
try:
    driver.get('https://www.google.com/travel/flights/')
    assert 'Find Cheap Flights Worldwide & Book Your Ticket - Google Flights' in driver.title

    elem = driver.find_element(By.XPATH, '//span[text()="Explore"')
    elem.click()
    WebDriverWait(driver, 10)
finally:
    driver.quit()