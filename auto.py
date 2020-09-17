import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

for i in range(0, 1000):
    chrome_options = Options()

    # incognito window
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.menti.com/3rt5hv13mk")

    radio = driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div[1]/form/fieldset/label[5]/div/span/label')

    radio.click()

    submit = driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div[1]/form/div/button')

    # take a pause 10 seconds
    submit.click()

    time.sleep(1)
    driver.close()
