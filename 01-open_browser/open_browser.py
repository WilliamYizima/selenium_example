from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep

options = Options()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
service = Service('C:/Program Files/Google/Chrome/Application/chromedriver.exe')
options.add_argument('--ignore-certificate-errors')
browser = webdriver.Chrome(options=options, service=service)

url = 'https://www.google.com.br'
xpath_input_find = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'

browser.get(url)
sleep(6)
input_find_in_page = browser.find_element_by_xpath(xpath_input_find)
print('vou clicar')
input_find_in_page.send_keys('testando o input no google')
input_find_in_page.send_keys(Keys.ENTER)
# input_find_in_page.click()
print('cliquei')
# browser.quit()