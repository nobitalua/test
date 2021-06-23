from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:/Users/Vi PHAM/AppData/Local/Programs/Python/Python310/Scripts/chromedriver")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_css_selector("input[type='checkbox']")
print(len(checkboxes))

for i in checkboxes:
  if i.get_attribute("value") == "option2":
      i.click()
      assert i.is_selected() #kt cac o da co check hay chua ?

radio = driver.find_elements_by_name("radioButton")
radio[2].click()
assert radio[2].is_selected()


#---------------------------------------kiem tra  hid/show button 

assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()