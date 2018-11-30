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
myurl = 'https://www.anz.co.nz/personal/home-loans-mortgages/mortgage-interest-rates/' 
  
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
stuff = mysoup.find("div", {'class':'tableContentInnerWrapper'})
stuff2 = stuff.findAll('td')
for i in range(0,len(stuff2)):
	stuff2[i] = stuff2[i].text.strip()

# extract the terms
_term = [None] * 7
_splrate = [None] * 7
_stndrate = [None] * 7
stuff2.insert(0,"")
i = 0
for j in range(0,7):
	_term[i] = stuff2[2+j*4]
	_splrate[i] = stuff2[3+j*4]
	_stndrate[i] = stuff2[4+j*4]
	i = i + 1

_list = [None] * 7
for i in range(0,7):
	_list[i] = "{0}   {1}    {2}".format("%-10s" % _term[i], "%12s" % _splrate[i], _stndrate[i])
	print(_list[i])
	print("")

file = open("anz_source.html", "w+", encoding ="utf-8")
for stf in stuff2:
	file.write(stf)
	file.write('\n')
file.close()
    
