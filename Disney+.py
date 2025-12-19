from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/")
driver.maximize_window()

# wait max 5 sec for page loading, then show "Load Error"
# implicitly_wait() is using for all other browsers
driver.implicitly_wait(5)

# this method is depreciated in Selenium4
# driver.find_element_by_name("q").send_keys("disney plus")
print(driver.find_element(By.NAME, "btnK").get_attribute("value"))  # Google button value
print(driver.find_element(By.NAME, "btnI").get_attribute("value"))  # Google second button value
driver.find_element(By.NAME, "q").send_keys("disney plus")
driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
time.sleep(2)

print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))  # Google logo image
# Same code, but with XPath locator
print(driver.find_element(By.XPATH, "//img[@title='Seasonal Holidays 2025']").get_attribute("src"))  # Google logo image
# print(driver.find_element(By.XPATH, '//*[@alt="2022 World Cup"]').get_attribute("src"))  # Google logo image


driver.implicitly_wait(3)
driver.back()


# Find element value, then store this value to variable "btnK"
btnK = driver.find_element(By.NAME, "btnK").get_attribute("value")
# Assert (compare) stored element value with required value
assert btnK == "Google Search"

# Same element verification for "Google Search" button
if btnK is not None:
    print("Google Search button is OK")
else:
    print("NO Google Search button")
time.sleep(3)
driver.find_element(By.NAME, "btnK").is_displayed()
print('------------------')
print(driver.find_element(By.NAME, "btnK").is_displayed())
#driver.find_element(By.NAME, "btnK").click()
#driver.back()
driver.find_element(By.NAME, "q").send_keys("disney plus")
# or just hit Enter on the Keyboard, code is below:
driver.find_element(By.NAME, "btnK").submit()

# Find and click on the DisneyPlus link
time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT, "Disney Plus").click()

# close Pop Up message
time.sleep(5)
driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.ESCAPE)
time.sleep(1)
try:
    assert "Disney+ | Stream Movies, TV Shows, Documentaries & More | U.S. Site" in driver.title
    print("Disney Plus Page Title is: ", driver.title)
except AssertionError:
    print("Disney Plus Page Title is different: ", driver.title)

time.sleep(3)

# Not common use
"""if "Disney+" not in driver.title:
    raise Exception("Title for Disney Plus page is wrong!")"""


# wait max 5 sec for page loading, then show "Load Error"
# set_page_load_timeout() is using for Chrome and FireFox mostly


driver.find_element(By.XPATH, "//a[@id='cjxdf3xnta1y6tbm']").click()

time.sleep(3)
driver.find_element(By.XPATH, "//div[@aria-label='Disney+ logo']//*[name()='svg']")
driver.find_element(By.XPATH, "//h1[normalize-space()='Enter your email to continue']").click()
time.sleep(0.5)
driver.back()
time.sleep(2)
# Find "New on Disney" and "Coming Soon" links by yourself


# First Card Text and Price verification
driver.find_element(By.XPATH, "//b[@class='display-small']")
driver.find_element(By.XPATH, "//span[contains(text(),'$12.99')]")

# Complete Text and Price verification for the second Card by yourself

# Third Card Text and Price verification
driver.find_element(By.XPATH, "//*[contains(text(),'Hulu') and contains(text(),'No Ads')]")
driver.find_element(By.XPATH, "//span[contains(text(),'$19.99')]")

# Button 1 click
driver.find_element(By.XPATH, "//*[contains(text(),'GET THIS OFFER')]").click()
time.sleep(3)

# Basic Page verification
titleBasicPlanPage = "Sign Up | Disney+"
assert titleBasicPlanPage in driver.title
#driver.find_element(By.ID, "nav-logo")
time.sleep(3)
driver.find_element(By.XPATH, "//button[@type='submit']")
driver.find_element(By.XPATH, "//input[@id='email']")
driver.find_element(By.ID, "email").send_keys("cibek55163@arugy.com")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[@data-testid='resend-primary']").click()
time.sleep(1)
#driver.find_element(By.XPATH, '//span[@class="sc-cHGsZl gaiHCy"]').click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(1)
#driver.find_element(By.ID, "email__error")

# Go back
driver.back()
# or code below
#driver.find_element(By.ID, "nav-logo").click()
driver.back()

mainPageTitle = "Disney+ | Stream Movies, TV Shows, Documentaries & More | U.S. Site"
if mainPageTitle == driver.title:
    print("Main Page Title is OK")
else:
    print("Main Page Title is Different")
    driver.save_screenshot("WrongTitleOnTheMainPage.png")

driver.find_element(By.XPATH, "//span[normalize-space()='New and upcoming from Disney+ and Hulu']")
time.sleep(3)
driver.find_element(By.XPATH, "//select[@aria-label='Select tab']").click()
time.sleep(0.5)


# Button 2 click
driver.find_element(By.XPATH, "//a[@data-testid='2p_bundle_cta']").click()
time.sleep(5)

# Advanced Page verification
titleAdvancedPlanPage = "Sign Up | Disney+"
assert titleAdvancedPlanPage in driver.title
# driver.find_element(By.XPATH, '//*[@class="sc-clNaTc kowWZm"]')
driver.find_element(By.XPATH, "//button[@type='submit']")
driver.find_element(By.XPATH, "//input[@id='email']")
time.sleep(1)

#driver.find_element(By.ID, "email").send_keys("")
driver.find_element(By.ID, "email").send_keys("cibek55163@arugy.com")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(1)
#//button[@data-testid='resend-primary']


driver.find_element(By.ID, "email")
#driver.find_element(By.XPATH, '//span[@class="sc-cHGsZl gaiHCy"]').click()
time.sleep(1)
#driver.find_element(By.XPATH, '//span[@class="sc-cHGsZl gaiHCy"]').click()
#driver.find_element(By.XPATH, "//button[contains(text(),'AGREE & CONTINUE')]").click()
time.sleep(1)
#driver.find_element(By.ID, "email__error")

# Go back
driver.back()
#driver.find_element(By.ID, 'logo-container').click()

if mainPageTitle == driver.title:
    print("Main Page Title is OK")
else:
    print("Main Page Title is Different")
    driver.save_screenshot("WrongTitleOnTheMainPage.png")

#driver.find_element(By.XPATH, '//*[@alt="Disney, Pixar, Marvel, Star Wars, National Geographic Logo"]')
driver.find_element(By.XPATH, "//body/div[@id='__next']/div[@class='redirect-preload-visibility is-visible']/div[@class='_2join21']/main/section[1]/div[1]/a[1]").click()
time.sleep(0.5)


# Button 3 click and Pro Page verification - Complete by yourself


# Find element value, then store this value to variable "DisneyPageLogo"
#DisneyPageLogoURL = driver.find_element(By.XPATH, '//*[@alt="Disney, Pixar, Marvel, Star Wars, National Geographic Logo"]').get_attribute("src")
#baseDisneyLogoURL = "https://cnbl-cdn.bamgrid.com/assets/8349a1f652e69bf1c3685a888092435110056a55e27b4eac3289e10fcb232978/original"
# Assert (compare) stored element value with required value
#assert DisneyPageLogoURL == baseDisneyLogoURL


DisneyPlusURL = "https://www.disneyplus.com/"
assert DisneyPlusURL == driver.current_url
if DisneyPlusURL != driver.current_url:
    print("Current 'Disney Plus' URL is different and it is: ", driver.current_url)
else:
    print("Current 'Disney Plus' URL is OK: ", driver.current_url)

# Same element verification for "Disney Plus Page Logo"
#DisneyPageLogo = driver.find_element(By.XPATH, '//*[@alt="Disney, Pixar, Marvel, Star Wars, National Geographic Logo"]')
"""if DisneyPageLogo:
    print("'Disney Plus' Page Logo is OK")
else:
    print("NO 'Disney Plus' Page Logo")"""

# Complete "Email" field on the Main page verification by yourself, using example above for "DisneyPageLogo"


# Click on invisible on the screen element
# Better to use "ActionChains" - example below - code line 220
page = driver.find_element(By.TAG_NAME, 'html')
page.send_keys(Keys.SPACE)
page.send_keys(Keys.SPACE)
page.send_keys(Keys.SPACE)
page.send_keys(Keys.SPACE)
time.sleep(2)

# First Plus button click and text verification
try:
    firstPlusButton = driver.find_element(By.XPATH, "//span[contains(text(),'What is Disney+?')]")
    if firstPlusButton:
        firstPlusButton.click()
    else:
        page.send_keys(Keys.SPACE)
        firstPlusButton.click()
except NoSuchElementException:


    time.sleep(1)
ButtonOneExpectedText = "Disney+ is the streaming home of Disney, Pixar, Marvel, Star Wars, National Geographic, " \
                        "and more. From new releases to your favorite classics and exclusive Originals, " \
                        "there's something for everyone. "
driver.find_element(By.XPATH, "//p[contains(text(),'Disney+ is the streaming home of Disney, Pixar, Ma')]")
ButtonOneActualText = driver.find_element(By.XPATH, "//p[contains(text(),'Disney+ is the streaming home of Disney, "
                                                    "Pixar, Ma')]").text
if ButtonOneExpectedText == ButtonOneActualText:
    print("Button One Text is OK")
else:
    print("Button One Text is DIFFERENT")
    print(driver.find_element(By.XPATH, "//p[contains(text(),'Disney+ is the streaming home of Disney, Pixar, Ma')]").text)
    driver.get_screenshot_as_file("Button One Different Text.png")
time.sleep(1)

# Second Plus button click and text verification
# Complete this assignment by yourself


secondPlusButton = driver.find_element(By.XPATH, "//span[contains(text(),'How much does Disney+ cost?')]")
if secondPlusButton:
    secondPlusButton.click()
else:
    page.send_keys(Keys.SPACE)
    secondPlusButton.click()

time.sleep(1)
driver.find_element(By.XPATH, "//p[contains(text(),'Access unlimited entertainment with Disney+ for $7')]")
time.sleep(1)

# Third Plus button click and text verification
# Complete this assignment by yourself
# Refer to "ActionChains" description: https://selenium-python.readthedocs.io/api.html
thirdPlusButton = driver.find_element(By.XPATH, "//p[contains(text(),'With Disney+, you can choose from an always-growin')]")
actions = ActionChains(driver)
actions.move_to_element(thirdPlusButton).perform()
time.sleep(1)
actions.click(thirdPlusButton).perform()

# Alternate choice for WebPage scrolling Down
page.send_keys(Keys.PAGE_DOWN)

time.sleep(1)
driver.find_element(By.XPATH, "//p[contains(text(),'With Disney+, you can choose from an always-growin')]")
thirdPlusButton_pointOne = driver.find_element(By.XPATH, "//p[contains(text(),'New releases and timeless classics')]")
time.sleep(1)

# Third Plus button - Point One text verification
# Complete this assignment by yourself for rest of the points text verification
thirdPlusButton_pointOne_ExpectedText = "New releases and timeless classics"
thirdPlusButton_pointOne_ActualText = driver.find_element(By.XPATH, "//p[contains(text(),'New releases and timeless classics')]").text
if thirdPlusButton_pointOne_ExpectedText == thirdPlusButton_pointOne_ActualText:
    print("Button 3 Text - Point 1 is OK")
else:
    print("Button 3 Text - Point 1 is DIFFERENT")
    print(driver.find_element(By.XPATH, "//p[contains(text(),'Disney+ is the streaming home of Disney, Pixar, Ma')]").text)
    driver.get_screenshot_as_file("Button 3 Text - Point 1 Different Text.png")
time.sleep(1)

# quit from browser
driver.quit()

# closing browser tab if you need to close just one Tab, but not the entire Browser
# driver.close()