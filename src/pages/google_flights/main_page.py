"""
Google Flights Page Object
"""
from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.consent_form.consent_page import ConsentPage

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

    def open(self, url: str = None):
        """
        Opens the Google Flights page and handles the consent form if it appears.
        """
        self.driver.get(self.URL if not url else url)
        self.handle_consent()

    def handle_consent(self):
        """
        Handles the consent form if it appears.
        """
        if self.driver.title == ConsentPage.TITLE:
            consent_page = ConsentPage(self.driver)
            consent_page.click_reject(self.min_action_delay, self.max_action_delay)
            self.wait.until(EC.title_contains(self.TITLE))

