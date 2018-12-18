import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from bs4 import BeautifulSoup as bs4

options = Options()
options.add_argument("--headless")

class Pesquisa:
    def __init__(self, driver=webdriver.Firefox(firefox_options=options)):
        self.driver = driver
        self.url = 'https://www.google.com/search?source=hp&ei=QxIYXNOAOcWewgSdxoVY&q=%22&btnK=Pesquisa+Google&oq=%22&gs_l=psy-ab.3..35i39l10.3524.3524..3952...2.0..0.129.226.1j1......0....1..gws-wiz.....6.n2q9JlJYQQc'
        self.search_bar = 'q' # name
        self.btn_search = 'Tg7LZd' # class
        self.img_google = 'hplogo' # id
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
        try:
            self.navigate()
            # adc texto na caixa de pesquisa e clica no btn pesuisa
            self.driver.find_element_by_name(self.search_bar).send_keys(word+'"')
            self.driver.find_element_by_class_name(self.btn_search).click()

            return self.driver.page_source
        except Exception as e:
            self.driver.quit()
            print(e)

    def parser(self, lista):
        """
        Método que faz a raspagem de dados.
        """
        # para cada palavra na lista, fara uma pesquisa
        for i in lista:
            page = bs4(self.search(i), 'html.parser')
            h3 = page.find_all('h3')
            # adicionara os tres primeiros h3 no dict response
            self.response[i] = {
                '1°': h3[0].text,
                '2°': h3[1].text,
                '3°': h3[2].text
            }
        self.driver.quit()
        return self.response
