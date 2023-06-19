from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

bot = webdriver.Chrome(service=servico)

if __name__ == "__main__":

    def loadpage(url):
        bot.get(url)

    def write_xpath(x_path, slep_time, number_attemps):
        bot.find_element('xpath', x_path).click    