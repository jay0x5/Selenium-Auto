#imports
from selenium import webdriver
import time
import json

#initialization
driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
driver.get("https://colab.research.google.com/?pli=1&authuser=0")


#Constants
LogMail = "stest1843@gmail.com"
LogPass = "shelltestonuk"

time.sleep(5)
fileo = open("collabcookies.json","r")
cookies = json.load(fileo)
print(cookies)
for cookie in cookies:
    cookie['domain'] = ".google.com"
    try:
        driver.add_cookie(cookie)
        print("added")

    except Exception as e:
        print(e)



