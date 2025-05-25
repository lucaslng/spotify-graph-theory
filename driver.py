from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from typing import List, Protocol
import undetected_chromedriver as uc

class Driver(Protocol):
  def implicitly_wait(self, time_to_wait: float) -> None: ...

  def get(self, url: str) -> None: ...

  def find_element(self, by: str = By.ID, value: str |
                   None = None) -> WebElement: ...

  def execute_script(self,
                     script,
                     *args
                     ): ...

  def find_elements(self,
                    by: str = By.ID,
                    value: str | None = None
                    ) -> List[WebElement]: ...

  def add_cookie(self, cookie_dict) -> None: ...

def create_brave_driver():
  options = ChromeOptions()
  options.binary_location = (
      "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
  )
  driver = webdriver.Chrome(options=options)
  driver.implicitly_wait(10)
  return driver


def create_safari_driver():
  options = SafariOptions()
  driver = webdriver.Safari(options=options)
  driver.implicitly_wait(10)
  return driver

def create_uc_driver():
  options = ChromeOptions()
  options.binary_location = (
      "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
  )
  driver = uc.Chrome(options=options, headless=False, use_subprocess=False)
  driver.implicitly_wait(10)
  return driver

def wait(driver: Driver, timeout=20) -> None:
  WebDriverWait(driver, timeout).until(  # type: ignore
      EC.presence_of_element_located((By.TAG_NAME, "body"))
  )

  driver.execute_script(
    "return document.readyState") == "complete"  # type: ignore
