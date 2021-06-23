import time

from selenium import webdriver

#driver = webdriver.Chrome(executable_path="C:/Users/Vi PHAM/AppData/Local/Programs/Python/Python310/Scripts/chromedriver")
#driver = webdriver.Firefox(executable_path="C:/Users/Vi PHAM/AppData/Local/Programs/Python/Python310/Scripts/geckodriver.exe")
#driver = webdriver.Edge(executable_path="C:/Users/Vi PHAM/AppData/Local/Programs/Python/Python310/Scripts/msedgedriver")

#driver.maximize_window()
#driver.get("https://vnexpress.net/")

#print(driver.current_url)
#print(driver.title)



#elements = driver.find_elements_by_css_selector("article.item-news")
#for el in elements:
#   print(el.text)

#driver.get("https://vnexpress.net/chang-trai-xay-nha-tu-go-vun-4296241.html")
#driver.minimize_window()
#driver.back()
#driver.refresh()
#driver.close()
#driver.quit()


###########################GHI CHU #####################################
########################################################################
############ WebDriver Locators: ID, Name, XPath, CSS, ClassName, linkText #############
#Customized CSS Syntax: tagname[attribute='value'] -- tagname optional
#Reg Ex: [attribute*='value']
##input[name='name']

#Customized Xpath Syntax:
#//tagname[@attribute=value] -- tagname optional
#Reg Ex: [contains(@attribute,'value')]
################################################################
################################################################


#------------------login gmail-----------------------------

#driver.maximize_window()
#driver.get("https://www.facebook.com/")
#driver.find_element_by_name("identifier").send_keys("nobitalua")
#driver.find_element_by_xpath("//input[@id='email']").send_keys("nobitalua")
#driver.find_element_by_xpath("//input[@id='pass']").send_keys("123")
#driver.find_element_by_xpath("//button[@name='login']").click()
#print(driver.find_element_by_xpath("//div[@class='_9ay7']").text)


#------------------login sale force-----------------------------
#driver.get("https://login.salesforce.com/")
#driver.maximize_window()
#driver.find_element_by_css_selector("#username").send_keys("nobitalua")
#driver.find_element_by_css_selector(".password").send_keys("123")
#driver.find_element_by_css_selector(".password").clear()
#driver.find_element_by_link_text("Forgot Your Password?").click()
#driver.find_element_by_xpath("//div[@class='verifyform']/input[3]").click()
#driver.find_element_by_css_selector("#username").send_keys("nobitalua")
#driver.find_element_by_css_selector(".password").send_keys("123")
#driver.find_element_by_xpath("//form[@id='login_form']/input[2]").click()
#print(driver.find_element_by_xpath("//form[@id ='login_form']/div[1]").text)

######phan nay chua co lay dc Xpath ma su dung text
#generate Xpath based on text
#//tagname[text()='xxx'] syntax
#driver.find_element_by_xpath("//a[text()='Cancel']").click()



#------------------login check for dropdown list static-----------------------------
#from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome(executable_path="C:/Users/Vi PHAM/AppData/Local/Programs/Python/Python310/Scripts/chromedriver.exe")
#driver.maximize_window()
#driver.get("https://rahulshettyacademy.com/angularpractice/")
# de su dung Select option thi bat buoc cai the tren dropdown list phai dung the select de coding
#dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
#dropdown.select_by_visible_text("Female")
#dropdown.select_by_index(0)
#print(driver.find_element_by_css_selector("div[class= 'form-group'] label[for='exampleFormControlSelect1']").text)



from selenium.webdriver.common.keys import Keys
#------------------login check for dropdown list dynamic-----------------------------
driver = webdriver.Chrome(executable_path="C:/Users/Vi PHAM/AppData/Local/Programs/Python/Python310/Scripts/chromedriver")
driver.get("https://www.makemytrip.com/")
#sai roi driver.find_element_by_xpath("//*[contains(@class ,'searchCity ')]/label").click()
#driver.find_element_by_css_selector("input[id='fromCity']").click()
driver.find_element_by_css_selector("input[id='fromCity']").click()
#driver.find_element_by_xpath("//input[@id='fromCity']").click()
#driver.find_element_by_id("fromCity").click()
#driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
time.sleep(2)
cities = driver.find_elements_by_xpath("//*[contains(@class,'blackText')]")

for city in cities:
    if city.text == "Del Rio, United States":
        print(city.text)
        city.click()
        break

driver.find_element_by_xpath("//p[text()='Delhi, India']").click()












#------------------condition-----------------------------
#ItemsInCart = 0

#Vi du su dung cau lenh condition
#if ItemsInCart != 2:
#   raise Exception("Product cart is not matching")
#pass

# vidu 2: co the su dung assert thay cho cau lenh dieu kien

#assert(ItemsInCart == 2) # assert chi su dung dieu kien dung /thoa man trong ngoac, trong truong hop, ko dung >>> thi quang ra error



#------------------exception-----------------------------
#try , except( su dung trong python, may ngon ngu khac su dung catch)



#vidu 1:
#with open('docbang.text', 'r') as reader:
 #   reader.read()



#vd 2 nay ,chi ra rang co loi thi quang ra thong bao nhu ben duoi, nhung ko biet loi do la loi gi
#try:
#    with open('docbang.text', 'r') as reader: # if have a exsited file named cuc.txt before, change the name to read then the message in catch block does not show up
#        reader.read()
#except:
 #   print("this is where an error message shown, since there is a failure in try block")




#vd3 trong cai nay, tiep voi vd o tren, thi se cho biet loi chinh xac dang gap phai
#try:
#    with open('docbang.text', 'r') as reader: # if have a exsited file named cuc.txt before, change the name to read then the message in catch block does not show up
#        reader.read()

#except Exception as e:
#    print(e)



#vd4 finally
# --- Finally còn được gọi là mệnh đề clean-up/termination vì nó luôn luôn chạy bất kể có lỗi nào xảy ra trong block try.
#Thường thì các câu lệnh trong finally được dùng để thực hiện công việc giải phóng tài nguyên.
#driver.close()

#try:
#    with open('docbang.text', 'r') as reader: # if have a exsited file named cuc.txt before, change the name to read then the message in catch block does not show up
#        reader.read()

#except Exception as e:
#    print(e)

#finally:
#    print("được gọi  đề clean-up/termination vì nó luôn luôn chạy bất kể có lỗi nào xảy ra trong block try.")

