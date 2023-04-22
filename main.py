from selenium import webdriver
from website import Website
from cookie import Cookie
from power_up import PowerUp
import time

languages = {
    "English": "langSelect-EN",
    "Portuguese": "langSelect-PT-BR",
    "Spanish": "langSelect-ES"
}

DURATION = 300
CHROMEDRIVER_PATH = "C:\\Dell\pythonprojects\\100_days_of_code\\day_48\\project\\chrome_driver\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
website = Website(driver)
website.open_site()
website.select_language(languages["English"])

cookie = Cookie(driver)
pwup = PowerUp(driver)
game_on = True
initial_time = time.time()
game_start = time.time()

while game_on:
    cookie.click_on_cookie()
    verification = pwup.verify_power_ups()
    try:
        pwup.get_higher_item()
    except ValueError:
        # Sometimes the program will not be able to get the elements from the page, resulting in an empty array of 
        # power ups. So if it happens, the program will restart the while loop, being successfull in the process.  
        continue
    else:
        last_time = time.time()
        if last_time - initial_time >= 5:
            # Every five seconds, the program will search for a new enabled power up, and set the previous index
            #And the higher power up available
            previous_index = pwup.previous_index
            higher_cost_index = pwup.higher_cost_index
            
            if previous_index != higher_cost_index and int(higher_cost_index) > int(previous_index):
                #The program will select a power up only once, so this conditional will see the index of the higher
                #power up available and the index of the previous power up. It will add only new power ups
                pwup.new_power_up()

        game_end = time.time()

        if game_end - game_start >= DURATION:
            #If it's true, it will end the game
            game_on = False

cookie.amount_cookie()
print(f"The total amount of cookies is: {int(cookie.amount)} cookies")
print(f"Cookies {cookie.per_second}")
