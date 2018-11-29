from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class signup():

    def testmethod(self):
        driver = webdriver.Firefox(executable_path=r"/home/pc-01/Documents/python/NEW/geckodriver")
        baseurl = "http://default-environment.i8pqpkc32a.us-west-2.elasticbeanstalk.com/"
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        time.sleep(5)

        #Scroll page from top to bottom

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(document.body.scrollHeight/4, document.body.scrollHeight/2);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(document.body.scrollHeight/2,(document.body.scrollHeight*3)/2);")
        time.sleep(2)
        driver.execute_script("window.scrollTo((document.body.scrollHeight*3)/2,document.body.scrollHeight);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        Title = driver.title
        print("Title of the page is: " + str(Title))

        #Create Account

        createaccount = driver.find_element(By.PARTIAL_LINK_TEXT, "Create")
        createaccount.click()

        Fname = driver.find_element(By.ID, "customer_first_name")
        Fname.send_keys("John")

        Lname = driver.find_element(By.ID, "customer_last_name")
        Lname.send_keys("Doe")

        email = driver.find_element(By.ID, "customer_email")
        email.send_keys("prasad+46@arkenea.com")

        password = driver.find_element(By.ID, "customer_password")
        password.send_keys("Qwerty@123")

        cpassword = driver.find_element(By.ID, "retype_customer_password")
        cpassword.send_keys("Qwerty@123")

        submit = driver.find_element_by_xpath("//input[@type='submit' and @value='Create Account']")
        submit.click()
        time.sleep(2)

        # Forgot your password

        forgotbutton = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot your password?")
        forgotbutton.click()

        forgotemail = driver.find_element(By.ID, "forgot_mail")
        forgotemail.send_keys("dangejasmine@gmail.com")

        submitbutton = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']")
        submitbutton.click()

        forgothere =driver.find_element(By.PARTIAL_LINK_TEXT, "Click here")
        forgothere.click()

        #Login

        logintext = driver.find_element(By.ID, "username")
        logintext.send_keys("dangejasmine@gmail.com")

        loginpassword = driver.find_element(By.ID, "password")
        loginpassword.send_keys("123456")

        loginbutton = driver.find_element_by_xpath("//input[@type='submit' and @value='Login']")
        loginbutton.click()

        time.sleep(2)
        driver.quit()

ff = signup()
ff.testmethod()
