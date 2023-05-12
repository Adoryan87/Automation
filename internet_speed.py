import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_driver_path = r"Users\Adoryan\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(options=options, service=Service(executable_path="chromedriver.exe", log_path="NUL"))
load_dotenv()

TWITTER_EMAIL = os.environ.get("EMAIL")
TWITTER_USERNAME = os.environ.get("USER")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = driver
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        driver.get(url="https://www.speedtest.net/")
        time.sleep(3)
        i_accept = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        go = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()

        time.sleep(70)
        self.down = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        time.sleep(3)



    def tweet_at_provider(self):
        driver.get(url="https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoicm8ifQ%3D%3D%22%7D")
        time.sleep(12)
        email = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.click()
        email.send_keys(TWITTER_EMAIL)
        next = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next.click()
        time.sleep(5)
        password = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(os.environ.get("USER"))
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(2)
        password1 = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password1.send_keys(os.environ.get("PASSWORD"))
        password1.send_keys(Keys.ENTER)
        time.sleep(30)
        tweet = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        tweet.click()
        time.sleep(2)
        tweet1 = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet1.click()
        text = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for 100 down/50 up?"
        tweet1.send_keys(text)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()