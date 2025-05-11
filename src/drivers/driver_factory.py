"""
# driver_factory.py
"""
from enum import Enum, auto
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


class AllowedBrowsers(Enum):
    """
    Enum for allowed browsers.
    """
    CHROME = auto()
    FIREFOX = auto()

def create_driver(browser=AllowedBrowsers.CHROME):
    """
    Factory function to create a WebDriver instance based on the specified browser.
    Args:
        browser (AllowedBrowsers): The browser to create a driver for.
    """
    if browser == AllowedBrowsers.CHROME:
        options = ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        return webdriver.Chrome(options=options)
