"""
Consent Form Page Object
"""
import random
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .consent_locators import ConsentLocators

class ConsentPage:
    """
    Page object for the google consent form page.
    """
    TITLE = "Before you continue"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_reject(self, min_delay, max_delay):
        """
        Clicks the reject button on the consent form.
        """
        button = self.wait.until(EC.element_to_be_clickable(ConsentLocators.REJECT_BUTTON))
        ActionChains(self.driver).pause(random.uniform(min_delay, max_delay)).click(button).perform()
