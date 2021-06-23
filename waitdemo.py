#implicit in Selenium
#explicit in selenium
#pause the test in Python using time class
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/Vi PHAM/AppData/Local/Programs/Python/Python310/Scripts/chromedriver")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
countabc = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert countabc == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for b in buttons:
    b.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector("span[class='promoInfo']").text)
