import random
from typing import Optional

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.consent_form.consent_page import ConsentPage
from .main_locators import MainLocators
from .explore_locators import ExploreLocators

class FlightsList:

    def __init__(self, driver: Optional[WebDriver]):
        self.driver = driver
        self.min_action_delay = 0.5
        self.max_action_delay = 0.9
        self.iterator = 0
        self.wait = WebDriverWait(driver, 10)
    
    def safe_find_all(self, locator, visible = False):
        """Always fetch fresh elements, waiting for presence or visibility."""
        if visible:
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def expand_all(self):
        button = self.safe_find_all(MainLocators.MORE_FLIGHTS_BUTTON, True)
        ActionChains(self.driver).move_to_element(button[0]).click(button[0]).perform()