from selenium import webdriver
import time

class InstagramAuto():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
    
    def auto_login(self):
        try:
            self.driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(3)
            inp_username = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
            inp_password = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
            btn_login = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
            inp_username.click()
            inp_username.send_keys(self.username)
            inp_password.click()
            inp_password.send_keys(self.password)
            time.sleep(1)
            btn_login.click()
        except Exception:
            print("Something went wrong!")
    
    def close_browser(self):
        self.driver.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.close()

bot = InstagramAuto("Your username, phone number or Email", "Your password")
bot.auto_login()
