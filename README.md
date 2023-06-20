# dyn-scrape

Basic script for dynamic content scraping.

## How to use this script

You need Python and Bash.

Clone this repo.

Make sure to have [Chrome](https://www.google.com/intl/us_us/chrome/) installed (Chromium should also work but it is not tested).  
You also need the correct [ChromeDriver](https://chromedriver.chromium.org/downloads) version.

Extract the driver and put the `chromedriver_linux64` folder in the dyn-scrape directory (same level as the template).

[template.py](https://github.com/vittoriocandolo/dyn-scrape/blob/main/template.py) already does most of the set up.  
Just edit the destination URL and the regex.

**Tested with Python 3.11.2, Chrome 114.0.5735.133 and ChromeDriver 114.0.5735.90 on Ubuntu 23.04**
