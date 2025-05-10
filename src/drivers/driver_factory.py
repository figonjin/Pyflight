from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from enum import Enum, auto

class AllowedBrowsers(Enum):
    CHROME = auto()
    FIREFOX = auto()

def create_driver(browser=AllowedBrowsers.CHROME):
    if browser == AllowedBrowsers.CHROME:
        options = ChromeOptions()
        # options.add_argument("user-data-dir=./chrome_pyflight")
        return webdriver.Chrome(options=options)
    # if browser == AllowedBrowsers.FIREFOX:
    #     options = FirefoxOptions()
    #     options.add_argument('-profile')
    #     options.add_argument('./firefox_pyflight')
    #     return webdriver.Firefox(options=options)
