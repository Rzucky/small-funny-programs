
####### terry talk inspired by Terry A. Davis who made a program to "talk to God"
####### made as a joke for fun
####### 03.01.2021

import linecache
import random

#choosing between 4 and 20 words to get some normal size text
n = random.randint(4,20)
terry = ''

for i in range(n):
	#english version has 108k words each in separate line
	#eng_k = random.randint(1,108386)

	#croatian version has 624k words each in separate line
	hrv_k = random.randint(1,624373)

	#English and Croatian version both made by Goran Igaly(https://github.com/gigaly), free non-commercial use
	#line = linecache.getline('EN_Txt-108.txt', eng_k)
	line = linecache.getline('HR_Txt-624.txt', hrv_k)

	#many lines have different number of tabs
	while '	' in line:
		line = line.replace('	', ' ')
	while '  ' in line:
		line = line.replace('  ', ' ')

	line = line.split(' ')
	#only the first word in line, others are not important
	word = line[0] + '  '
	terry += word

#clearcache is good practice to do after using linecache.getline()
linecache.clearcache()

print(terry)
