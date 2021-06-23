from selenium import webdriver

# cac option cu Chrome Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(executable_path="C:/Users/Vi PHAM/AppData/Local/Programs/Python/Python310/Scripts/chromedriver", options=chrome_options)
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
print(driver.title)