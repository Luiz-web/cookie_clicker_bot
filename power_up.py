from selenium.webdriver.common.by import By
import time

class PowerUp:
    # Class responsible for assigning power ups in game.
    def __init__(self, driver):
        self.driver = driver
        self.enabled_power_ups = None
        self.previous_index = -1.1
        self.higher_cost_index = 1.0
        self.power_up_prices = None

    def verify_power_ups(self):
        self.enabled_power_ups = self.driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
        self.get_price_power_ups()
        
    def get_price_power_ups(self):
        self.power_up_prices = []
        for power_up in self.enabled_power_ups:
            power_up = power_up.text
            cost = power_up.split("\n")[1]
            cost = cost.replace(",", "")
            self.power_up_prices.append(float(cost))
            
    def get_higher_item(self):
        higher_cost_item = max(self.power_up_prices)
        self.higher_cost_index = self.power_up_prices.index(higher_cost_item)

    def new_power_up(self):
        time.sleep(5)
        higher_power_up = self.enabled_power_ups[self.higher_cost_index]
        try:
            higher_power_up.click()
        except:
            #If the program fails to click on the power up, due to the page's processing, it will call this method again
            self.new_power_up()
        else:
            self.previous_index = self.higher_cost_index


