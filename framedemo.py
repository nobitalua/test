from selenium import webdriver

driver = webdriver.Chrome(executable_path ="C:/Users/Vi PHAM/AppData/Local/Programs/Python/Python310/Scripts/chromedriver")
driver.get("https://the-internet.herokuapp.com/iframe")
#using frameid, framename or index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("chay tu dong")

driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)