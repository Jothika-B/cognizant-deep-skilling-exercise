from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Maximize window
driver.maximize_window()

# Open website
driver.get("https://example.com")

# Print page title
print("Page Title:", driver.title)

# Wait for 3 seconds
time.sleep(3)

# Find the heading element
heading = driver.find_element(By.TAG_NAME, "h1")
print("Heading:", heading.text)

# Close browser
driver.quit()
