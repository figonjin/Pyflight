import random
from typing import Optional

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.consent_form.consent_page import ConsentPage
from .main_locators import MainLocators
from .explore_locators import ExploreLocators

class MainPage:
    """
    Google Flights Page Object
    """
    URL = "https://www.google.com/travel/flights/"
    TITLE = "Google Flights"

    def __init__(self, driver: Optional[WebDriver]):
        if driver is None:
            raise ValueError("A valid WebDriver instance must be provided.")
        self.driver = driver
        self.min_action_delay = 0.5
        self.max_action_delay = 0.9
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """
        Opens the Google Flights page and handles the consent form if it appears.
        """
        self.driver.get(self.URL)
        self.handle_consent()

    def handle_consent(self):
        """
        Handles the consent form if it appears.
        """
        if self.driver.title == ConsentPage.TITLE:
            consent_page = ConsentPage(self.driver)
            consent_page.click_reject(self.min_action_delay, self.max_action_delay)
            self.wait.until(EC.title_contains(self.TITLE))

    def click_explore(self):
        """
        Clicks the 'Explore' button on the Google Flights page.
        """
        button = self.wait.until(EC.element_to_be_clickable(MainLocators.EXPLORE_BUTTON))
        ActionChains(self.driver).pause(random.uniform(self.min_action_delay, self.max_action_delay)).click(button).perform()
        self.wait.until(EC.visibility_of_element_located(ExploreLocators.MAP_TAG))
