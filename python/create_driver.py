from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

def create_driver() -> WebDriver:
	options = Options()
	options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
	driver = webdriver.Chrome(options=options)
	driver.implicitly_wait(10)
	return driver