#imports
from selenium import webdriver
import time
import json

#initialization
driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
driver.get("https://colab.research.google.com/?pli=1&authuser=1")

#Constants
LogMail = "stest1843@gmail.com"
LogPass = "shelltestonuk"

#Functions
def Login():

    #Sign-In
    signIn_button = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/div/div/a")
    signIn_button.click()

    #enter mail
    mail_input_field = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    mail_input_field.send_keys(LogMail)

    #click on next button
    next_button = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
    next_button.click()

    time.sleep(2)

    # #enter password
    password_input_field = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    password_input_field.send_keys(LogPass)

    # time.sleep(2)

    # #submit button
    submit_button = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
    submit_button.click()
    time.sleep(10)
    cookies = driver.get_cookies()
    cookies = json.dumps(cookies, indent=4)

    #save cookies to json

    with open("collabcookies.json", "w+") as jfile:
        jfile.write(cookies)


time.sleep(5) # a 5sec sax sux wait
Login()

    



