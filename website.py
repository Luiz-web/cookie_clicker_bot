from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Website:
    #Class responsible for the website elements and its respective attributes
    def __init__(self, driver):
        self.url = "https://orteil.dashnet.org/cookieclicker/"
        self.language = None
        self.driver = driver
        self.start_on_google()

    def start_on_google(self):
        self.driver.get("https://www.google.com")
        time.sleep(5)
        search_bar = self.driver.find_element(By.CLASS_NAME, value='gLFyf')
        search_bar.send_keys("Cookie Clicker")
        search_bar.send_keys(Keys.ENTER)
        time.sleep(5)


    def open_site(self):
        site = self.driver.find_element(By.CSS_SELECTOR, value='.LC20lb.MBeuO.DKV0Md')
        site.click()
        time.sleep(10)

    def select_language(self, language):
        self.language = language
        language_choice = self.driver.find_element(By.ID, value=self.language)
        language_choice.click()
        time.sleep(10)


