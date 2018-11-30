# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import datetime
# import requests
import time
from selenium import webdriver
# import selenium

##=================================================================================
save2htmlpath = 'E:\\PythonExercises\\'
myurl = 'https://www.westpac.co.nz/home-loans/your-home-loan-options/choices-fixed/' 
  
# # retrieve page from internet
print('Retrieve data from Internet ...')
##=================================================================================        
mydriver = webdriver.Firefox()
mydriver.set_window_size(0, 0)
mydriver.set_window_position(0, 0)

mydriver.get(myurl)
time.sleep(7)  # wait js to complete

# extract source code
mypage = mydriver.page_source
mydriver.quit()

mysoup = BeautifulSoup(mypage, 'lxml')
stuff = mysoup.find("div", {'id':'tab3'})
stuff2 = stuff.findAll('td')

for i in range(0,len(stuff2)):
	stuff2[i] = stuff2[i].text.strip()
	
del stuff2[0]
del stuff2[0]

for stf in stuff2:
	print(stf)
	
file = open("anz_source.html", "w+", encoding ="utf-8")
for stf in stuff2:
	file.write(stf)
	file.write("\n")
file.close()
    
