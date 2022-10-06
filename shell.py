#imports
from selenium import webdriver
import time
import json

#initialization
driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
driver.get("https://cloud.google.com/shell/?utm_source=google&utm_medium=cpc&utm_campaign=japac-IN-all-en-dr-bkwsrmkt-all-all-trial-e-dr-1009882&utm_content=text-ad-none-none-DEV_c-CRE_602384344538-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20Management%20Tools%20~%20Cloud%20Shell_cloud%20shell-general%20-%20Products-KWID_43700071544381595-kwd-837034669893&userloc_9303477-network_g&utm_term=KW_gcp%20cloud%20shell&gclid=EAIaIQobChMI5eKF3v_K-gIV3JNmAh3ipgWkEAAYASAAEgIjd_D_BwE&gclsrc=aw.ds")

#Constants
LogMail = "stest1843@gmail.com"
LogPass = "shelltestonuk"

#Functions
def Login():

    #Sign-In
    signIn_button = driver.find_element_by_xpath("/html/body/section/devsite-header/div/div[1]/div/div/devsite-user/div/a")
    signIn_button.click()

    # #enter mail
    mail_input_field = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    mail_input_field.send_keys(LogMail)

    # #click on next button
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

    with open("cookies.json", "w+") as jfile:
        jfile.write(cookies)


time.sleep(5) # a 5sec sax sux wait
Login()

    



