from selenium import webdriver
from login_page import LoginPage
from home_page import HomePage

driver = webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")

login = LoginPage(driver)
login.login("student", "Password123")

home = HomePage(driver)
print("Page Title:", home.get_title())

driver.quit()
