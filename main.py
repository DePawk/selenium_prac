import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Browser:
    browser,serivce = None, None

    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service = self.service)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by = by, value = value)
        button.click()
        time.sleep(1)

    def vote_royals(self, username: str):
        self.add_input( by = By.NAME, value = "name", text = username)
        self.click_button(by = By.NAME, value = "gtop")

if __name__ == "__main__":
    browser = Browser("C:/webdriver/chromedriver.exe")
    browser.open_page('https://mapleroyals.com/?page=vote')
    time.sleep(5)

    browser.vote_royals("enter username here")
    time.sleep(20)

