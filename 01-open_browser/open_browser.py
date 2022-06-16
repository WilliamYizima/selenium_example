from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


options = Options()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
service = Service('C:/Program Files/Google/Chrome/Application/chromedriver.exe')
browser = webdriver.Chrome(options=options, service=service)