from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Data:
    url = 'https://www.saucedemo.com/'
    Username = 'standard_user'
    password = 'secret_sauce'

class Locator:
    userName_locator = 'user-name'
    password_locator = 'password'
    loginButton_locator = 'login-button'

class Fetch_details(Data,Locator):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def start_automation(self):
        self.driver.get(Data.url)
        self.driver.maximize_window()
        print("Web page automated successfully")
        sleep(5)
    
    def Login(self):
        self.driver.find_element(by=By.ID, value = self.userName_locator).send_keys(self.Username)
        self.driver.find_element(by=By.ID, value = self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.ID, value = self.loginButton_locator).click()
        print("Successfully logged in")
         
    def Fetch_title(self):
        print(self.driver.title)

    def Fetch_url(self):
        print(self.driver.current_url)
    
    def Fetch_pageSource(self):
        page_content = self.driver.page_source
        with open('Webpage_task_11.txt','a') as file:
            file.write(page_content)

    def shutdown(self):
        self.driver.quit()
        print("Web page shutdown successfully")

myfetch = Fetch_details()
myfetch.start_automation()
myfetch.Login()
myfetch.Fetch_title()
myfetch.Fetch_url()
myfetch.Fetch_pageSource()
myfetch.shutdown()

        