from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from graphtypes import UserNode

from driver import Driver, wait

import time

def parse_followee(element: WebElement) -> UserNode | None:
	
	aria = element.get_attribute('aria-labelledby')
	assert aria is not None
	aria = aria.removeprefix('card-title-spotify:')
	if aria.startswith('artist'):
		return None
	assert aria.startswith('user:')
	id = aria.removeprefix('user:').split('-')[0]


	img_url = ""
	try:
		img_url = element.find_element(By.TAG_NAME, 'img').get_attribute('src')
	except NoSuchElementException:
		pass
	finally:
		assert img_url is not None

	name = element.find_element(By.XPATH, './/div[4]/div/a/p/span/span').text

	return UserNode(id, name, img_url)


def scrape(driver: Driver, target_id: str):

	# print("scraping:", target_id)

	# scrape
	url = f'https://open.spotify.com/user/{target_id}/' # following or followers

	driver.get(url + 'following')

	wait(driver)

	time.sleep(4.5)

	following_elements = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[2]/div[5]/div/div[2]/div[1]/div/main/section/div/section/div[3]/div')

	following_users: set[UserNode] = set(filter(lambda x: x is not None, map(parse_followee, following_elements))) # type: ignore

	# print(following_users)
	
	# time.sleep(500000)
	return following_users
