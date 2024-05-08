from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import logging
import scraper2 as scraper
import time
import undetected_chromedriver as uc


def login():
    driver.get("https://www.tiktok.com/login/phone-or-email/email")
    time.sleep(5)

    # driver.find_element(By.XPATH, '//input[contains(@name,"username")]').send_keys(username)
    # time.sleep(2)

    # driver.find_element(By.XPATH, '//input[contains(@type,"password")]').send_keys(password)
    # time.sleep(2)

    # driver.find_element(By.XPATH, '//button[contains(@data-e2e,"login-button")]').click()
    time.sleep(40)


if __name__ == '__main__':
    logger = logging.Logger('catch_all')

    # Configure webdriver options for stealth scraping
    options = webdriver.chrome.options.Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("start-maximized")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTMLi, like Gecko) "
        "Chrome/110.0.0.0 Safari/537.36")
    options.add_argument("--accept-lang=en-US,en;q=0.5")
    options.add_argument("--dom-automation=disabled")

    driver = uc.Chrome(headless=False, use_subprocess=False)

    # options.add_argument('--user-data-dir=C:\\Users\\sahaa.000\\AppData\\Local\\Google\\Chrome\\User Data')

    # options.add_argument('--profile-directory=Person 1')

    # driver = webdriver.Chrome(options=options)

    # driver.get("https://www.tiktok.com")
    
    actions = ActionChains(driver, duration=550)

    # TODO: Change this to bot_info/bots.json
    # Get login information from bots configurations
    # with open('bot_info/bots.json', 'r') as f:
    #     data = json.load(f)

    # # TODO: update bot name
    # username = data['botA6']['user_name']
    # password = data['botA6']['account_password']

    username = 'reddy5463'
    password = 'FG456Reddy@'

    login()

    scraper.begin_scrape(driver)
    driver.quit()
