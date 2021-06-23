from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:/Users/Vi PHAM/AppData/Local/Programs/Python/Python310/Scripts/chromedriver")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
chuoi = "tuong vi"

driver.find_element_by_css_selector("#name").send_keys(chuoi)
driver.find_element_by_id("alertbtn").click()

alert = driver.switch_to.alert
texta = alert.text

assert chuoi in texta
alert.accept()
#alert.dismiss() # for cancel



