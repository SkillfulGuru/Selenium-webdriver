# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import datetime
# import requests
import time
from selenium import webdriver
# import selenium

save2htmlpath = 'E:\\PythonExercises\\'
myurl = 'https://www.anz.co.nz/personal/home-loans-mortgages/mortgage-interest-rates/' 
  
# # retrieve page from internet
print('Retrieve data from Internet ...')
     
mydriver = webdriver.Firefox()
mydriver.set_window_size(0, 0)
mydriver.set_window_position(0, 0)

mydriver.get(myurl)
time.sleep(7)  # wait js to complete
    
mypage = mydriver.page_source
mydriver.quit()

mysoup = BeautifulSoup(mypage, 'lxml')
stuff = mysoup.find("div", {'class':'tableContentInnerWrapper'})
stuff2 = stuff.findAll('td')
for i in range(0,len(stuff2)):
	stuff2[i] = stuff2[i].text.strip()

file = open("anz_source.html", "w+", encoding ="utf-8")
for stf in stuff2:
	file.write(stf)
	file.write('\n')
file.close()
    
