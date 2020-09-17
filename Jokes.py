import os
from datetime import date
import re
import ssl
import requests
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

from urllib import request
import json
jokes=['']
for j in range(1,10):
    resp = request.urlopen("http://www.laughfactory.com/jokes/yo-momma-jokes/"+str(j))
    text = resp.read()
    plaintext=text.decode('utf8')
    # print(plaintext)
    soup=BeautifulSoup(plaintext,'html.parser')
    search=soup.find_all('div',attrs={'class':"joke-text"})
    
    
    for para in search:
        # print(para.p.text)
        jokes.append(para.p.text)
        


chrome_options = Options()

# incognito window
# chrome_options.add_argument('--headless')
# chrome_options.add_argument("--incognito")
chrome_options.add_argument('user-data-dir=C:\\Users\\Ayush Rungta\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://web.whatsapp.com")
input("Press")
# time.sleep(15)
search=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search.click()
contact=input("Enter contact : ")
search.send_keys(contact)
time.sleep(1)
selected_contact = driver.find_element_by_css_selector('span[title="'+contact+'"]')
selected_contact.click()
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = driver.find_element_by_xpath(inp_xpath)
# time.sleep(20)

for each in jokes:
    input_box.send_keys(each + Keys.ENTER)
    # time.sleep(2)
