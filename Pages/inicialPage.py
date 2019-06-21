from selenium.webdriver.common.keys import Keys
class InicialPage():

    def __init__(self, driver):
        self.driver = driver

        self.campoPesquisa_input_xpath = "//input[@name = 'q']"
        self.botaoPesquisa_input_xpath = "(//input[@value = 'Pesquisa Google'])[2]"


    def digitar_pesquisa(self, texto):
        self.driver.find_element_by_xpath(self.campoPesquisa_input_xpath).clear()
        self.driver.find_element_by_xpath(self.campoPesquisa_input_xpath).send_keys(texto)


    def enter_pesquisa(self):
        self.driver.find_element_by_xpath(self.campoPesquisa_input_xpath).send_keys(Keys.ENTER)