#This program asks the user to input the email recipient and the message they want to send them, 
#and then logs into the user's outlook account and sends a new email to the imput email recipient, 
#containing the user input text. Thanks for not abusing the email address.

import os, requests, bs4, re
from selenium import webdriver

print('Hello, who is the recipient of the email?')
emailAddress = input()
isEmail=re.compile(r'[a-z0-9]+((\.|\_)[a-z0-9]+)*@[a-z0-9]+(\.[a-z0-9]+)*(\.[a-z0-9]{2,20})')
mo = isEmail.search(emailAddress)
if mo:
	True
else:
	print('That is not a valid email address')
print('And what do you wish to tell them?')
textString = input()

browser = webdriver.Firefox()
browser.get('https://outlook.live.com/owa/')
blueLargeButton=browser.find_element_by_class_name('buttonLargeBlue')
blueLargeButton.click()
browser.implicitly_wait(20)
emailElement = browser.find_element_by_css_selector('.placeholder')
emailElement.send_keys('testingPurposesMelina@hotmail.com')
nextButton = browser.find_element_by_id('idSIButton9')
nextButton.click()
passwordElement = browser.find_element_by_css_selector('#i0118')
passwordElement.send_keys('Thanksfornotabusing!')
browser.implicitly_wait(20)
signinButton = browser.find_element_by_css_selector("#idSIButton9[value='Sign in']")
signinButton.click()
newEmail = browser.find_element_by_id('_ariaId_24')
newEmail.click()
browser.implicitly_wait(20)
sendTo = browser.find_element_by_class_name('_fp_F')
sendTo.send_keys(emailAddress)
browser.implicitly_wait(20)
textBox = browser.find_element_by_css_selector('.ConsumerCED')
browser.implicitly_wait(20)
textBox.send_keys(textString)
subjectBox = browser.find_element_by_css_selector('._mcp_Q1')
subjectBox.send_keys("That's a random subject so that I don't get the warning popup")
sendButton = browser.find_element_by_css_selector('button._mcp_62')
sendButton.click()
