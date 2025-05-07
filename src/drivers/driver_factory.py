from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

from enum import Enum, auto

class AllowedBrowsers(Enum):
    CHROME = auto()
    FIREFOX = auto()

def create_driver(browser=AllowedBrowsers.CHROME):
    if browser == AllowedBrowsers.CHROME:
        options = ChromeOptions()
        options.add_argument("user-data-dir=./chrome_pyflight")
        return webdriver.Chrome(options=options)