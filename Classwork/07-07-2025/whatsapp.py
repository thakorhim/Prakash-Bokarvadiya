from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import os

def download_profile_picture(contact_name):
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com")
    input("📱 Please scan the QR code and press ENTER...")

    # Search and open chat
    search_box = driver.find_element(By.XPATH, '//div[@title="Search input textbox"]')
    search_box.click()
    time.sleep(1)
    search_box.send_keys(contact_name)
    time.sleep(2)

    contact = driver.find_element(By.XPATH, f'//span[@title="{contact_name}"]')
    contact.click()
    time.sleep(2)

    # Open profile drawer
    header = driver.find_element(By.XPATH, '//header')
    header.click()
    time.sleep(3)

    # Get profile picture URL
    try:
        img = driver.find_element(By.XPATH, '//img[contains(@src,"blob:")]')
        src = img.get_attribute("src")
        print("📷 Profile Pic URL:", src)

        # Download image
        img_data = requests.get(src).content
        filename = f"{contact_name}_dp.jpg"
        with open(filename, 'wb') as f:
            f.write(img_data)
        print(f"✅ Profile picture saved as {filename}")
    except:
        print("❌ Profile picture not found or private.")

    driver.quit()

# Main function
if __name__ == "__main__":
    contact = input("Enter contact name as saved in WhatsApp: ")
    download_profile_picture(contact)
