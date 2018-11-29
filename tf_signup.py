from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path=r"/home/pc-01/Downloads/chromedriver")
driver.get('http://default-environment.i8pqpkc32a.us-west-2.elasticbeanstalk.com/')
driver.maximize_window()

time.sleep(5)
#Redirect to Create account button
driver.find_element_by_partial_link_text('Create').click()

driver.find_element(By.ID, "customer_first_name" ).send_keys("John")
driver.find_element(By.ID, "customer_last_name" ).send_keys("Doe")
driver.find_element(By.ID, "customer_email").send_keys("abc18@yopmail.com")
driver.find_element(By.ID, "customer_password").send_keys("Qwerty@123")
driver.find_element(By.ID, "retype_customer_password").send_keys("Qwerty@123")
driver.find_element_by_xpath("//input[@type='submit' and @value='Create Account']").click()
time.sleep(5)


#Test credentials
#dangejasmine@gmail.com
#123456

#Redirect to login page from sign up page ->

driver.find_element_by_partial_link_text('My Account').click()

#login page 
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("dangejasmine@gmail.com")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()

time.sleep(5)

driver.quit()

#Radio button handling using select command
import time
radiobuttons = dirver.find_elements(By.id, "catDropdown")
size = len(radiobuttons)
print ("The size is:" +str(size))

#Drop-down handling using select command
element = driver.find_element_by_id("select_sort")
sel = Select(element)

sel.select_by_index(2)
print("It should select preorder")
time.sleep(2)

sel.select_by_value("oldest")
print("It should select oldest")
time.sleep(2)

sel.select_by_visible_text("Price: Lowest First")
print("It should select Price: Lowest First")
time.sleep(2)


#Mouse hover -

from selenium.webdriver.common.action_chains import ActionChains

element_to_hover_over = driver.find_element_by_xpath("//div/div[2]/div/div[2]")	#Feature preorders - Masterminds creation item no. 2 

hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()	#if clicked more info button is visible

print("Element visible?" + str(element_to_hover_over.is_displayed()))	#True if visible, false if hidden

#####
Created class -> need init method (to perform driver class)
Class h():
def __init__(self, driver):
self.driver = driver
######

Calendar - xppath - //section[@class='cal-month'][position()=1]//a[text()='3']


#How to take screenshots

destinationFileName = "/users/atomar/Desktop/test.png"             	#path

try : 
	driver.save_screenshot(destinationFileName)
	print("screenshot saved to :" + destinationFileName)
except NotaDirectoryError:
	print("Not a directory issue")

#Find size of the window

height = driver.execute_script("return_window.innerheight;")
width = driver.execute_script("return_window.innerwidth;")
print("Height: " + str(height))
print("width: " + str(width))


	
