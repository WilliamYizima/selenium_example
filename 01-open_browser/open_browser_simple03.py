from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

# Enter the necessary variables
url = 'https://www.google.com.br'
xpath_input_find = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'

# Open  browser and go to url
browser.get(url)

# 'wait' load website
sleep(6)

# find element of HTML
input_find_in_page = browser.find_element_by_xpath(xpath_input_find)

# 'type' in element 
input_find_in_page.send_keys('testando o input no google')
print('digitando')

# 'press enter' in element
input_find_in_page.send_keys(Keys.ENTER)
print('cliquei')

# uncomment if you want quit your browser with Selenium
# browser.quit()