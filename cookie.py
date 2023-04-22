from selenium.webdriver.common.by import By
import time

class Cookie:
    #Class responsible for the cookie and its respectives elements and attributes
    def __init__(self, driver):
        self.driver = driver
        self.cookie = self.driver.find_element(By.ID, value="bigCookie")
        self.amount = None
        self.per_second = None

    def click_on_cookie(self):
        self.cookie.click()

    def amount_cookie(self):
        time.sleep(5)
        cookies_quantity = self.driver.find_element(By.ID, value='cookies').text
        self.per_second = cookies_quantity.split('\n')[1]
        quantity = cookies_quantity.split(" ")[0]
        quantity_replaced = quantity.replace(",", "")
        self.amount = float(quantity_replaced)

        