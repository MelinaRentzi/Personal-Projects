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
emailElement.send_keys('r.melina_92@hotmail.com')
nextButton = browser.find_element_by_id('idSIButton9')
nextButton.click()
passwordElement = browser.find_element_by_css_selector('#i0118')
passwordElement.send_keys('sugar453232sweet')
browser.implicitly_wait(20)
signinButton = browser.find_element_by_css_selector("#idSIButton9[value='Sign in']")
signinButton.click()
newEmail = browser.find_element_by_id('_ariaId_24')
newEmail.click()
sendTo = browser.find_element_by_class_name('_fp_F')
sendTo.send_keys(emailAddress)
textBox = browser.find_element_by_css_selector('.ConsumerCED')
browser.implicitly_wait(20)
textBox.send_keys(textString)
sendButton = browser.find_element_by_css_selector('div._mcp_g1')
sendButton.click()