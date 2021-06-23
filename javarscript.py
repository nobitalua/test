from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:/Users/Vi PHAM/AppData/Local/Programs/Python/Python310/Scripts/chromedriver")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Tuong Vi")

print(driver.find_element_by_name("name").text)

#--------------seleinum ho tro de in gia tri trong texbox ,su dung thuoc tinh get aatribute
print(driver.find_element_by_name("name").get_attribute("value"))

#-----------trong th ko co su dung dc selenium thi su dung javarscript

print(driver.execute_script('return document.getElementsByName("name")[0].value'))

#-----------su dung javascript de click thay vi su dung selenium
temp = driver.find_element_by_css_selector("a[href*='shop']")

driver.execute_script("arguments[0].click();",temp)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")