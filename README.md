## Instagram Scraper

This repository contains a script that scrapes Instagram posts for specific information and saves this information to an Excel spreadsheet. The script uses Selenium for automation, BeautifulSoup for HTML parsing, and openpyxl for Excel operations. The script logs into Instagram, navigates to a specific profile, scrolls down to load all posts, clicks on each post, and extracts the content of the post.

## Environment Variables

To run this script, you need to settwo environment variables:

1. 'INSTAGRAM_USERNAME': The username of the Instagram account.
2. 'INSTAGRAM_PASSWORD': The password of the Instagram account.

You can set the environment variables in your terminal using the following commands:

´´´bash
export INSTAGRAM_USERNAME='turnkeyofficespace'
export INSTAGRAM_PASSWORD='Cv3+;37VUnG&'

## Prerequisites

To run this script, you need:

- Python 3.x
- Selenium
- BeautifulSoup
- openpyxl
- A Google Chrome browser
- ChromeDriver (make sure it's compatible with your Chrome version)

## Setup

1. Clone the repository
2. Install the required Python packages: pip install -r requirements.txt
## Configuration

Before running the script, you need to configure the following variables in the script:

- PROFILE_NAME: The Instagram profile from which to scrape the posts.
- NUM_POSTS_TO_SCRAPE: The number of posts to scrape.
- OUTPUT_FILE_NAME: The name of the output Excel file.
- chrome_driver_path: The path to your ChromeDriver executable.

## Running the Script

To run the script, simply execute the Python file from your terminal:

´´´bash
python3 igScraper.py

Output:
The script will create an excel spreadsheet with the name specified in OUTPUT_FILE_NAME. The spreeahsheet will contain the data scraped from the Instagram posts.

Please note that you have to be logged in to Instagram to scrape data from it. As scraping can violate Instagram's terms of service, please use this script responsibly and only scrape data that you are authorized to access.

## Logging

This script uses Python's built-in `logging` module to provide status updates and debugging information. These logs can help you understand what the script is doing, and they can be very useful for troubleshooting if something goes wrong.

The level of detail in the logs is controlled by the log level, which is set to `INFO` by default. This means that informational messages, warnings, and errors will be logged, but more detailed debug messages will not. You can change the log level to `DEBUG` if you need more detailed logs for troubleshooting.

Here's what the different log levels mean:

- `DEBUG`: Detailed information, typically useful only when diagnosing problems. This level includes everything.
- `INFO`: Confirmation that things are working as expected. This is the default log level.
- `WARNING`: An indication that something unexpected happened, or there may be some issue in the near future (e.g., 'disk space low'). The software is still working as expected.
- `ERROR`: More serious problem that prevented the software from performing some function.
- `CRITICAL`: A very serious error that may prevent the program from continuing to run.

The log messages will be printed to the console as the script runs. Look for these messages to understand what the script is doing and to identify any problems.

Example of a log message:

´´´bash
INFO:root:Successfully logged in with username: your_username



