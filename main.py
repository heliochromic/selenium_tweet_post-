from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PROMISED_DOWN = 150
PROMISED_UP = 0
CHROME_DRIVER_PATH = ""
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""
URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/home"

chrome_driver_path = Service(executable_path=CHROME_DRIVER_PATH)


class InternetSpeedTwitterBot:

    def __init__(self, chrome_driver_path_class):
        self.driver = webdriver.Chrome(service=chrome_driver_path_class)
        self.down: float = 0
        self.up: float = 0

    def get_internet_speed(self):
        self.driver.get(URL)
        go = self.driver.find_element(By.CLASS_NAME, "start-text")
        go.click()
        sleep(90)
        self.down = float(self.driver.find_element(By.XPATH,
                                                   '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH,
                                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        print(f"down: {self.down}\nup: {self.up}")

    def tweet_at_provider(self):
        self.driver.get(url=TWITTER_URL)
        self.driver.implicitly_wait(5)
        email = self.driver.find_element(By.XPATH,
                                         '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        self.driver.implicitly_wait(5)

        try:
            username = self.driver.find_element(By.CSS_SELECTOR,
                                                "input.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")
            username.send_keys("wawyyyyi")
            username.send_keys(Keys.ENTER)
        except NoSuchElementException:
            pass

        self.driver.implicitly_wait(5)
        password = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        # find the element log in
        # request using xpath
        # clicking on that element

    def post_tweet(self):
        self.driver.implicitly_wait(5)

        text_field = self.driver.find_element(By.CSS_SELECTOR,
                                              "div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
        text_field.send_keys(f"logged in dudes")
        self.driver.implicitly_wait(5)
        try:
            text_field.send_keys(Keys.ENTER)
        except StaleElementReferenceException:
            pass
        self.driver.implicitly_wait(5)
        tweet_button = self.driver.find_element(By.CSS_SELECTOR,
                                                "div#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-kemksi.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(3) > div > div > div:nth-child(2) > div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr > div")
        self.driver.implicitly_wait(5)
        tweet_button.click()
        print("tweet is published")


bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.tweet_at_provider()
bot.post_tweet()
