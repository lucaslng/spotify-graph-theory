import time

from driver import Driver

def login(driver: Driver, session_token: str) -> None:
	driver.get("https://accounts.spotify.com")

	time.sleep(1)

	driver.add_cookie({ # this is the one cookie that is required
    "name": "sp_dc",
    "value": session_token,
		"domain": ".spotify.com",
    "path": "/",
    "expires": -1,
    "httpOnly": True,
    "secure": True
  })

	time.sleep(1)

	driver.get("https://accounts.spotify.com")



# old login method that was very bad

# def login(driver: Driver, email: str, pwd: str) -> None:

# 	print("Logging in...")

# 	driver.get('https://accounts.spotify.com/en/login')
# 	time.sleep(0.2)
# 	wait(driver)
# 	driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/input').send_keys(email)

# 	try:
# 		driver.implicitly_wait(0)
# 		time.sleep(0.4)
# 		driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[2]/input')
# 	except NoSuchElementException:
# 		print("password box not found")
# 		driver.implicitly_wait(10)
# 		driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/button/span[1]/span').click()
# 		time.sleep(3)
# 		driver.find_element(By.XPATH, '/html/body/div/div/div[2]/main/div/div/div/div/form/div[2]/section/button').click()
# 		time.sleep(3)
# 	finally:
# 		time.sleep(0.2)
# 		driver.implicitly_wait(10)
# 		driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[2]/input').send_keys(pwd)
# 		driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/button/span[1]/span').click()
# 		time.sleep(3)


# 	# user_name = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div[3]').text
# 	# return user_name

# 	# try:
# 	# 	driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div[2]/svg/path')
# 	# except NoSuchElementException:
# 	# 	target_img = None
# 	# else:
# 	# 	target_img = None # TODO: set to image