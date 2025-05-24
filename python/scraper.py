from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from graphtypes import UserNode
import time

def wait(driver: WebDriver, timeout=20) -> None:
	WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
	
	driver.execute_script("return document.readyState") == "complete" # type: ignore

def parse_followee(element: WebElement) -> UserNode | None:
	
	aria = element.get_attribute('aria-labelledby')
	assert aria is not None
	aria = aria.removeprefix('card-title-spotify:')
	if aria.startswith('artist'):
		return None
	assert aria.startswith('user:')
	id = aria.removeprefix('user:')[:-2]
	
	img_url = element.find_element(By.TAG_NAME, 'img').get_attribute('src')
	assert img_url is not None

	name = element.find_element(By.XPATH, './/div[4]/div/a/p/span/span').text

	return UserNode(id, name, img_url)


def scrape(driver: WebDriver, target_id: str):

	# scrape
	url = f'https://open.spotify.com/user/{target_id}/' # following or followers
	time.sleep(2)
	driver.get(url + 'following')

	wait(driver)

	following_elements = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[2]/div[5]/div/div[2]/div[1]/div/main/section/div/section/div[3]/div')

	following_users = set(filter(lambda x: x is not None, map(parse_followee, following_elements)))

	print(following_users)
	
	time.sleep(500000)

# def scrape_all(target_id: str, steps: int) -> :
