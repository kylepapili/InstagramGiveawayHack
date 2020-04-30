import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def login(username, password, driver):
    driver.get("https://www.instagram.com/accounts/login/")
    count = 0
    while count < 15:
    	try:
    		username_element = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
    		password_element = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
    		break
    	except:
    		time.sleep(1)
    		count = count + 1
    		print(count)
    username_element.send_keys(username)
    password_element.send_keys(password)
    login_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
    login_button.click()
    time.sleep(2)
    driver.get("https://www.instagram.com/"+username)
    
def get_followers(driver):
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
    time.sleep(1)
    scroll_div = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
    previous_height = 0
    current_height = 1
    while previous_height != current_height:
        previous_height = current_height
        current_height = driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;', scroll_div)
        time.sleep(1)
        if(previous_height == current_height):
            time.sleep(2)
            current_height = driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;', scroll_div)
    list_of_users = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul')
    items = list_of_users.find_elements_by_tag_name('li')
    usernames = []
    for item in items:
        username_element = item.find_element_by_class_name('FPmhX');
        usernames.append(username_element.text)
    driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
    return usernames

def get_following(driver):
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
    time.sleep(1)
    scroll_div = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
    previous_height = 0
    current_height = 1
    while previous_height != current_height:
        previous_height = current_height
        current_height = driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;', scroll_div)
        time.sleep(1)
        if(previous_height == current_height):
            time.sleep(2)
            current_height = driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;', scroll_div)
    list_of_users = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul')
    items = list_of_users.find_elements_by_tag_name('li')
    usernames = []
    for item in items:
        username_element = item.find_element_by_class_name('FPmhX');
        usernames.append(username_element.text)
    driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
    return usernames