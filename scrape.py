import logging
import sys

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def access_webpage(url, driver_path):

    options = Options()
    options.add_argument("--headless")
    
    service = Service(driver_path)
    with webdriver.Chrome(service=service, options=options) as driver:
        try:
            driver.get(url)
            page_content = driver.page_source
            return page_content
        except WebDriverException as e:
            logger.error(f"Error accessing the web page: {e}")
            return None

def save_page_content(content, filename):
    
    if content is not None:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        logger.info(f"Page content saved to file {filename}")
    else:
        logger.error("Unable to save the page content.")

if len(sys.argv) > 1:
    URL = sys.argv[1]
else:
    URL = "https://www.example.com"

DRIVER_PATH = 'chromedriver_linux64/chromedriver'

page_content = access_webpage(URL, DRIVER_PATH)
save_page_content(page_content, 'page.html')
