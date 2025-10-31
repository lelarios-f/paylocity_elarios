import os
import pytest
import logging
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


CHROME_DRIVER_PATH = ChromeService(ChromeDriverManager().install())

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode."
    )

@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--allow-file-access-from-files")
    options.add_argument("--allowfile-access")
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(service=CHROME_DRIVER_PATH, options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()
  