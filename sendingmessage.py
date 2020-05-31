from selenium import webdriver # installing the webdriver
driver = webdriver.Chrome() # initializing the webdriver for chrome! 

driver.get('https://web.whatsapp.com/') # URL for the page
driver.maximize_window()

name = input("Enter name or group name:") 
msg = input("Enter message: ")

seq = int(input())


user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

for word in range(seq):
	msg_box.send_keys(msg)
	driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

print('Success')
