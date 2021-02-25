from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

print('started')
file = open('fizikakodovi.txt', 'r')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome("C:/Users/Roko/AppData/Local/chromedriver.exe", chrome_options=chrome_options)

driver.get('https://osnove.tel.fer.hr/anovo/asp/ulaz.asp')

for i in range(30): 

	try:
		line = file.readline()
		jmbag = line[2:]
		
		print(f'{i}. - {jmbag}')

		inputMBroj = driver.find_element_by_name('mbroj')

		inputMBroj.send_keys(jmbag)
		time.sleep(.5)
		#finds the button and presses it
		ActionChains(driver).click(driver.find_elements_by_class_name('in1')[2]).perform()

		driver.refresh()

	except:
		print('found one')
		time.sleep(0.5)
		driver.refresh()
		#opens in new tab to save info
		driver.execute_script('''window.open("https://osnove.tel.fer.hr/anovo/asp/ulaz.asp","_blank");''')
		time.sleep(0.5)
		#to stop it from iterating while we check succesfull entry
		input()
		driver.refresh()

print('done')