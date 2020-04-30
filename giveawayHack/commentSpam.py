import AcquireDataFunctions as dataFun
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

# generate random integer values
from random import seed
from random import randint
followersFile = open("followers.txt","r") 
followingFile = open("following.txt", "r")
followers = followersFile.readlines()
following = followingFile.readlines()

with open('randomAccounts.csv', newline='') as f:
    reader = csv.reader(f)
    accountsList = list(reader)

def commentSpam(link, driver):
	driver.get(link)
	time.sleep(5)
	commentBox = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div[1]")
	usersSent = [""];
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	while len(usersSent) < 49:
		try:
			commentBox.click()
			textBox = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div[1]/form/textarea')
			textBox.send_keys(accountsList[len(usersSent)][0])
			textBox.send_keys(Keys.ENTER)
			usersSent.append(accountsList[len(usersSent)][0])
			time.sleep(15)
		except:
			time.sleep(1)

u=open("username.txt", "r")
username = u.read()

p = open("password.txt", "r")
password = p.read()

driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
dataFun.login(username, password, driver)
commentSpam("https://www.instagram.com/p/B_dpJ9xpDzS/", driver)