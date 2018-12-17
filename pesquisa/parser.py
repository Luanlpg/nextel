from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from bs4 import BeautifulSoup as bs4

options = Options()
options.add_argument("--headless")

class Pesquisa:
    def __init__(self, driver=webdriver.Firefox(firefox_options=options)):
        self.driver = driver
        self.url = 'http://google.com.br'
        self.search_bar = 'lst-ib' # id
        self.btn_search = 'btnK' # name
        self.response = {}

    def navigate(self):
        """
        Navega até url pré-definina.
        """
        self.driver.get(self.url)

    def search(self, word=''):
        """
        Faz busca de de resultados.
        """
        self.navigate()
        # adc texto na caixa de pesquisa e clica no btn pesuisa
        self.driver.find_element_by_id(self.search_bar).send_keys(word)
        self.driver.find_element_by_name(self.btn_search).click()

        return self.driver.page_source

    def parser(self, lista):
        """
        Método que faz a raspagem de dados.
        """
        # para cada palavra na lista, fara uma pesquisa
        for i ins lista:
            page = bs4(self.search(i), 'html.parser')
            h3 = page.find_all('h3')
            # adicionara os tres primeiros h3 no dict response
            self.response[i] = {
                '1°': h3[0],
                '2°': h3[1],
                '3°': h3[2]
            }
        return self.response
