from selenium import webdriver
from getpass import getpass

username = 'Artorius'
password = 'Rembombino512'

driver = webdriver.Chrome("C:\\Drivers\\WebDriver\\chromedriver.exe")
driver.get("https://cabinet.vvsu.ru/")

username_textbox = driver.find_element_by_id("login")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("password")
password_textbox.send_keys(password)

login_button = driver.find_element_by_id("accept")
login_button.submit()