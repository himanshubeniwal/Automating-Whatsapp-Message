# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 01:07:11 2020

@author: Himanshu Beniwal
"""

from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com/')
driver.maximize_window()

name = input("Enter name or group name:")
#msg = input("Enter message: ")

seq = list(input('Enter message:').split())


user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

for word in seq:
	msg_box.send_keys(word)
	driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

print('Success')
