from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def scrape(username: str, pwd: str, target_id: str) -> None:
	options = Options()
	options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
	driver = webdriver.Chrome(options=options)
	driver.implicitly_wait(10)
	driver.get('https://accounts.spotify.com/en/login')

	# login
	driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/input').send_keys(username)
	driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/button/span[1]/span').click()
	driver.find_element(By.XPATH, '/html/body/div/div/div[2]/main/div/div/div/div/form/div[2]/section/button').click()
	driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[2]/input').send_keys(pwd)
	driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/button/span[1]/span').click()

	# scrape
	url = f'https://open.spotify.com/user/{target_id}/' # following or followers
	time.sleep(1)
	driver.get(url + 'following')

	following = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[2]/div[5]/div/div[2]/div[1]/div/main/section/div/section/div[3]/div')
	print(len(following))

	# followers = driver.find_elements(By.XPATH, ...)

	
	time.sleep(500000)