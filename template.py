import csv
import logging
import os
import re
import subprocess
from datetime import datetime

URL = "" # FIXME
HTML = "page.html"
CSV = "data.csv"

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

venv_folder = "venv"
init_script = "init.sh"
scraping_script = "scrape.sh"

if not os.path.exists(venv_folder):
    logger.info(f"Virtual environment folder '{venv_folder}' does not exist.")
    logger.info("Running init script to set up the environment...")
    try:
        subprocess.run(["bash", init_script, URL], check=True)
        logger.info("Virtual environment set up successfully.")
    except subprocess.CalledProcessError:
        logger.error("Failed to set up the virtual environment. Aborting script.")
        exit(1)

logger.info("Running scraping script...")
try:
    subprocess.run(["bash", scraping_script], check=True)
    logger.info("Scraping script completed successfully.")
except subprocess.CalledProcessError:
    logger.error("Failed to run the scraping script.")

with open(HTML, "r", encoding="utf-8") as file:
    page_content = file.read()
    match = re.search(r'', page_content) # FIXME
    if match:
        value = match.group(1)
    else:
        value = None

current_date = datetime.now().strftime("%Y-%m-%d") # FIXME

if not os.path.exists(CSV):
    with open(CSV, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Value"]) # optional
    logger.info(f"Created CSV file: {CSV}")

try:
    with open(CSV, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([current_date, value])
    logger.info(f"Value added to CSV file: {current_date}, {value}")
except IOError:
    logger.error("Failed to append value to CSV file.")
