from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path ="C:/Users/Vi PHAM/AppData/Local/Programs/Python/Python310/Scripts/chromedriver")
#driver.get("https://www.familysearch.org/en/")

#ACTIONCHAINS -- DUNG DE DIEU KHIEN CHO MAY CAI SUB MENU

action = ActionChains(driver)

#action.move_to_element(driver.find_element_by_id("search")).perform()

#action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()


#action.move_to_element(driver.find_element_by_xpath("//button[text()='Search']")).click().perform()
#action.move_to_element(driver.find_element_by_xpath("//a[@data-config='lo_hdr9_srch:genealogies']")).click().perform()

#action.move_to_element(driver.find_element_by_xpath("//iframe[@id='mce_0_ifr']")).perform()
#action.move_to_element(driver.find_element_by_xpath("//nav[@id='primaryNav']/div[2]/ul/li[4]")).click().perform()


#--------------------double click click by using ACTION seleniumd
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

#action.context_click(driver.find_element_by_id("double-click")).click().perform()
action.double_click(driver.find_element_by_id("double-click")).click().perform()
alert = driver.switch_to.alert

assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()

#-----------------------------content click by using ACTION seleniumd, right click
action.context_click(driver.find_element_by_id("double-click")).click().perform()




