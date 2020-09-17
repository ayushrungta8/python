import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = Options()

# incognito window
chrome_options.add_argument('--headless')
# chrome_options.add_argument("--incognito")
chrome_options.add_argument('user-data-dir=C:\\Users\\Ayush Rungta\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://web.whatsapp.com")
time.sleep(15)
search=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search.click()
contact=input("Enter Contact : ")
search.send_keys(contact)
time.sleep(1)
# selected_contact = driver.find_element_by_xpath("//span[@title={'Hritique'}]")
selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
while(True):
    input_box.send_keys('' + Keys.ENTER)
    # time.sleep(2)
# allCookies = driver.get_cookies
# driver.get("https://web.whatsapp.com")
# driver.add_cookie(allCookies)
# # time.sleep(10)

# print (allCookies)