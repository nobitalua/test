#implicit in Selenium
#explicit in selenium
#pause the test in Python using time class
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:/Users/Vi PHAM/AppData/Local/Programs/Python/Python310/Scripts/chromedriver")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
countabc = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert countabc == 3
list = []
list2 = []
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
#//div[@class='product-action']/button/parent::div/parent::div/h4  ra 1 cap thi dung dau parent::the can ra
for b in buttons:
    list.append(b.find_element_by_xpath("parent::div/parent::div/h4").text)
    b.click()
print(list)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 15)


wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
veggies = driver.find_elements_by_css_selector("p.product-name")
for v in veggies:
    list2.append(v.text)
print(list2)
#so sanh 2 cai list
assert list == list2
originalAmount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span[class='promoInfo']")))
discountAmount = driver.find_element_by_css_selector(".discountAmt").text
#kt coi gia co giam sau khi nhap ma discount ko
assert float(discountAmount) < int(originalAmount)


print(driver.find_element_by_css_selector("span[class='promoInfo']").text)



amount = driver.find_elements_by_xpath("//tbody/tr/td[5]")
sum = 0
for t in amount:
     sum = sum + int(t.text)
print(sum)

totalAmount = int(driver.find_element_by_class_name("totAmt").text)

assert sum == totalAmount
