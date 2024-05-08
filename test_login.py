from selenium import webdriver

options = webdriver.ChromeOptions() 

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

options.add_argument('--user-data-dir=C:\\Users\\sahaa.000\\AppData\\Local\\Google\\Chrome\\User Data')

options.add_argument('--profile-directory=Person 1')

driver = webdriver.Chrome(options=options)

driver.get("https://www.tiktok.com")