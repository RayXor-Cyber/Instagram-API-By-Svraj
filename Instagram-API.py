from selenium import webdriver
from selenium.webdriver.common.by import By
from instagrapi import Client  # Hypothetical library
import time
import logging

# Configure logging
logging.basicConfig(filename="errors.log", level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Selenium driver
driver = webdriver.Chrome() 

# Prompt for target account and account to follow
target_account = input("Enter the target account username: ")
account_to_follow = input("Enter the account to follow: ")


# Navigate to the target account's followers list
driver.get(f"https://www.instagram.com/{target_account}/followers/")

# Extract usernames (simplified example)
usernames = []
while True:
    try:
        for element in driver.find_elements(By.XPATH, "//a[@href]/span"):
            username = element.text
            usernames.append(username)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    except:
        break

driver.quit()

# Initialize Instagram API client (hypothetical)
cl = Client()
cl.login("<username>", "<password>")  # Only for hypothetical API interaction

# Loop through usernames and send follow requests
for username in usernames:
    try:
        cl.follow(account_to_follow)  # Follow the specified account
        print(f"Followed {account_to_follow} on behalf of {username}")
        time.sleep(5)  # Add a delay to avoid rate limiting
    except Exception as e:
        logging.error(f"Error following {account_to_follow} on behalf of {username}: {e}")
        print(f"Error following {account_to_follow} on behalf of {username}: {e}")

print("Process complete.") 



