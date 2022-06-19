from time import sleep

from selenium import webdriver

browser = webdriver.Chrome()

url = 'https://www.google.com.br'
xpath_input_find = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'

browser.get(url)
sleep(6)

input_find_in_page = browser.find_element_by_xpath(xpath_input_find)

input_find_in_page.send_keys('testando o input no google')
print('digitando')

# uncomment if you want quit your browser with Selenium
browser.quit()