from selenium import webdriver
from random import randint
from random import choice
from datetime import date
import requests
import string
import time
import os
import re
def Find(string):
    # findall() has been used
    # with valid conditions for urls in string
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url

def upvoteSite():
	profile = webdriver.FirefoxProfile()
	profile.set_preference("network.proxy.type", 1)
	profile.set_preference("network.proxy.socks", '127.0.0.1')
	profile.set_preference("network.proxy.socks_port", 9050)
	profile.set_preference("network.proxy.socks_remote_dns", True)
	profile.set_preference("browser.privatebrowsing.autostart", True)
	profile.update_preferences()
	driver = webdriver.Firefox(firefox_profile=profile)

	try:
		print('Clearing all cookies...')
		driver.delete_all_cookies()

		print('Setting up anonymous web identity...')
		driver.get("https://moonwatchers.cc/Coin&id=28")


		print('Search for Upvote Button')
		time.sleep(randint(1,5))
		driver.find_element_by_xpath('//*[@id="body-section"]/div/div/div/div[2]/div/div[1]/div[2]/h4/a/button').click()


		print('Restarting')
		driver.delete_all_cookies()
		print('Clearing cookies...')
		time.sleep(5)
		driver.close()
		return
	except:
		print('Error. Trying again...')
		driver.close()
		time.sleep(30)
		upvoteSite()
		return

def main():
	times = int(input('Enter number of upvotes \n'))
	for i in range(times):
		os.system('service tor restart')
		upvoteSite()
		print('System cooldown')
		time.sleep(15)
main()
