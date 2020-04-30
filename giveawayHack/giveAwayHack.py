import AcquireDataFunctions as dataFun
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

u=open("username.txt", "r")
username = u.read()

p = open("password.txt", "r")
password = p.read()

driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
dataFun.login(username, password, driver)
followers = dataFun.get_followers(driver)
following = dataFun.get_following(driver)

print(followers)
print(following)

file1 = open("followers.txt","w+") 
file1.write(str(followers))
file1.close() 
file2 = open("following.txt", "w+")
file2.write(str(following))
file2.close()