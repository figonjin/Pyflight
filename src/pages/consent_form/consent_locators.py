"""
This file contains the locators for the Google Consent Form page.
"""
from selenium.webdriver.common.by import By

class ConsentLocators:
    """
    Locators for Google Consent Form page elements.
    """
    REJECT_BUTTON = (By.CSS_SELECTOR, "[aria-label='Reject all'] [aria-hidden='true']")
