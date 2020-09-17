import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


chrome_options = Options()

# incognito window
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument('--headless')
# chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://newspaperpdf.online/download_the_hindu.php")

radio = driver.find_element_by_xpath(
   '//*[@id="containerid"]/ul/li[1]/a')

radio.click()
time.sleep(2)

submit = driver.find_element_by_xpath(
    '/html/body/div[3]/div[3]/div/div[3]/div[2]/div[2]/div[3]')

# take a pause 10 seconds
submit.click()
time.sleep(10)
# driver.close()
