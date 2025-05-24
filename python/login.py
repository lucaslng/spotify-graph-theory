from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


import time


def login(driver: WebDriver, username: str, pwd: str):
	driver.get('https://accounts.spotify.com/en/login')
	time.sleep(0.2)

	driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/input').send_keys(username)

	try:
		driver.implicitly_wait(0)
		driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[2]/input')
	except NoSuchElementException:
		print("password box not found")
		driver.implicitly_wait(10)
		driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/button/span[1]/span').click()
		driver.find_element(By.XPATH, '/html/body/div/div/div[2]/main/div/div/div/div/form/div[2]/section/button').click()
	finally:
		driver.implicitly_wait(10)
		driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[2]/input').send_keys(pwd)
		driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/button/span[1]/span').click()


	# user_name = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div[3]').text
	# print('user_name:', user_name)

	# try:
	# 	driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div[2]/svg/path')
	# except NoSuchElementException:
	# 	target_img = None
	# else:
	# 	target_img = None # TODO: set to image