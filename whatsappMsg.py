from selenium import webdriver
import time

# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('/path/to/chromedriver')

driver.get("https://web.whatsapp.com/")
input("Scan the QR code and then press Enter")

# Replace 'Friend's Name' with the name of your WhatsApp friend or group
target = '"Friend\'s Name"'

# Replace the below string with your own message
message = "Hello, this is a test message sent from Python!"

# Searches for the target in the chats list and clicks on it
driver.find_element_by_css_selector("._3FRCZ").click()
time.sleep(2)

# Types the message in the message box and hits the send button
input_box = driver.find_element_by_xpath("//div[@class='_2A8P4']//div[@class='_1Plpp']")
input_box.send_keys(message)
time.sleep(2)
driver.find_element_by_xpath("//button[@class='_35EW6']//span[@data-testid='send']").click()
time.sleep(2)

print("Message sent successfully!")
driver.quit()
