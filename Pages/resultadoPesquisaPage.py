class ResultadoPesquisaPage():

    def __init__(self, driver):
        self.driver = driver

        self.imagens_a_xpath = "//a[text() = 'Imagens']"

    def clicar_imagens(self):
        self.driver.find_element_by_xpath(self.imagens_a_xpath).click()

