from selenium import webdriver
import unittest
from Pages.inicialPage import InicialPage
from Pages.resultadoPesquisaPage import ResultadoPesquisaPage
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from datetime import datetime
from Resources.Report.evidencia import Evidencia
from Resources.Functions.Reader import getProperty

class funcionalidadeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=getProperty("chromedriver_path"))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.ambiente = "Teste"
        self.startTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


    def test_pesquisa_google_sol(self):
        driver = self.driver

        evidencia = Evidencia(driver)
        pg_inicial = InicialPage(driver)
        pg_pesquisa = ResultadoPesquisaPage(driver)

        self.test_name = self._testMethodName
        self.error_msg = None

        try:
            driver.get("https://www.google.com")
            evidencia.screenshot("Acessar Google")
            pg_inicial.digitar_pesquisa("Sol")
            evidencia.screenshot("Pesquisar Sol")
            pg_inicial.enter_pesquisa()
            evidencia.screenshot("Resultado")
            pg_pesquisa.clicar_imagens()
            evidencia.screenshot("Imagens")

            self.status = "Passou"
            self.error_msg = None

        except Exception as e:
            self.error_msg = str(e)
            evidencia.screenshot("Falha")
            self.status = "Falhou"


    def test_pesquisa_google_lua(self):
        driver = self.driver

        evidencia = Evidencia(driver)
        pg_inicial = InicialPage(driver)
        pg_pesquisa = ResultadoPesquisaPage(driver)

        self.test_name = self._testMethodName

        try:
            driver.get("https://www.google.com")
            evidencia.screenshot("Acessar Google")
            pg_inicial.digitar_pesquisa("Lua")
            evidencia.screenshot("Pesquisar Lua")
            pg_inicial.enter_pesquisa()
            evidencia.screenshot("Resultado")
            pg_pesquisa.clicar_imagens()
            evidencia.screenshot("Imagens")

            self.status = "Passou"
            self.error_msg = None

        except Exception as e:
            self.error_msg = str(e)
            evidencia.screenshot("Falha")
            self.status = "Falhou"

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        self.endTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        Evidencia.gerar_evidencia(self, self.test_name, self.ambiente,self.status, self.startTime,
                                  self.endTime, self.error_msg)
        Evidencia.limpar_screenshot(self)



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=getProperty("html_report_path")))
