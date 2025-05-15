# John Lester Banasihan
# Automating the SauceDemo webpage

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver
driver = webdriver.Chrome()

# Open the web application
driver.get("https://www.saucedemo.com/")

# Initialize the elements needed before doing actions + initializing the explicit waits for the elements
let username_field = await driver.find_element(By.ID, "user-name")
let password_field = await driver.find_element(By.ID, "password")
let login_button = await driver.find_element(By.ID, "login-button")
let add_item_to_cart = await driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
let your_cart_items = await driver.find_element(By.Class, "shopping_cart_link")
let remove_item_to_cart = await driver.find_element(By.Class, "remove-sauce-labs-backpack")


# Enter credentials and login to the page
username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
login_button.click()

#Add item and Assert the added item
add_item_to_cart.click()
your_cart_items.click()

assert_the_cart_items = driver.find_element(By.Class, "cart_item")
if len(assert_the_cart_items) > 0:
    print("The element is existing and the assertion is passed!✅")
else:
    print("The element is not existing!❌")

#Delete item
remove_item_to_cart.click()


# Validate login success
assert "inventory" in driver.title

dashboard_of_saucedemo_page = driver.find_element(By.Class, "app_logo")
if len(dashboard_of_saucedemo_page) > 0:
    print("The element is existing and the assertion is passed!✅")
else:
    print("The element is not existing!❌")
finally:
# Close the browser
driver.quit()
print("Test execution completed.")