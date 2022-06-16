from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

options = Options()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
service = Service('C:/Program Files/Google/Chrome/Application/chromedriver.exe')
options.add_argument('--ignore-certificate-errors')
browser = webdriver.Chrome(options=options, service=service)

url = 'https://ge.globo.com/mg/triangulo-mineiro/noticia/2022/06/16/com-direito-a-recorde-mundial-gabriel-bandeira-vence-200m-medley-no-mundial-de-natacao-paralimpica.ghtml'
xpath_input_find = '/html/body/div[2]/div[1]/header/div[2]/div/div/span/a'

browser.get(url)
sleep(6)
input_find_in_page = browser.find_element_by_xpath(xpath_input_find)
print('vou clicar')
input_find_in_page.click()
print('cliquei')
# browser.quit()