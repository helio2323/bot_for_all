from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from .modules import loadpage, write_xpath
from time import sleep

servico = Service(ChromeDriverManager().install())

bot = webdriver.Chrome(service=servico)

loadpage("https://www.eneba.com/br/")

bot.maximize_window

sleep(3000)

write_xpath('//*[@id="app"]/main/div/div[2]/section[1]/section/div/div[1]/div/div/div[3]/a')