form_link = "https://docs.google.com/forms/d/e/1FAIpQLScz8ceNM6KGeG2hhqVPmeVJa989-AohcxN_sOU9kowQ5RNHFw/viewform?usp=sf_link"

zillow = "https://appbrewery.github.io/Zillow-Clone/"

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)




response = requests.get(zillow)
contents = response.text
soup = BeautifulSoup(contents, "html.parser")

addys = soup.find_all("address")
addys_text = [item.getText().replace("\n","").replace("|", '').strip() for item in addys]

house_prices = soup.find_all(class_= 'PropertyCardWrapper')
prices = [item.getText().replace("/mo", "").split("+")[0].replace("\n",'') for item in house_prices if str(item)]

house_links = soup.find_all(class_ = "StyledPropertyCardDataArea-anchor")
links = [links.get("href") for links in house_links]

print(addys_text)
print(prices)
print(links)

for n in range(len(prices)):

    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScz8ceNM6KGeG2hhqVPmeVJa989-AohcxN_sOU9kowQ5RNHFw/viewform?usp=sf_link")

    property_address = driver.find_element(By.CLASS_NAME, "whsOnd")
    price_per_month = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_property = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    button = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")


    property_address.send_keys(addys_text[n])
    price_per_month.send_keys(prices[n])
    link_property.send_keys(links[n])


    button.click()

