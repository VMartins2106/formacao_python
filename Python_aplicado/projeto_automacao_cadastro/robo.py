from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# CÓDIGO SEM TRATAMENTO DE ERROS

def cadastro_web(dataframe):
    browser = webdriver.Chrome() # Abertura do chrome
    browser.maximize_window() # Maximizando a janela do chrome
    browser.get('http://automacao.empowerdata.com.br/') # Entra no site desejado

    email = browser.find_element(By.XPATH, '//*[@id="email"]') # Acha o input do email a ser informado no site
    email.send_keys('aluno@empowerdata.com.br') # Cola o email no campo selecionado
    
    # email.send_keys(Keys.TAB) Isto dá tab, para ir o próximo input
    login = browser.find_element(By.XPATH, '//*[@id="password"]') # Acha o input da senha a ser informado no site
    login.send_keys('empowerpython') # Cola a senha no campo selecionado

    time.sleep(1)

    botao_entrar = browser.find_element(By.XPATH, '//*[@id="submit"]') # Acha o input do botão a ser clicado no site
    botao_entrar.click() # Clica no botão

    time.sleep(3)

    # Iterando sobre as linhas do dataFrame
    for _, linha in dataframe.iterrows():
        nome_cliente = browser.find_element(By.XPATH, '//*[@id="nome"]')
        nome_cliente.send_keys(linha['Nome'])

        email_cliente = browser.find_element(By.XPATH, '//*[@id="email"]')
        email_cliente.send_keys(linha['E-mail'])

        telefone_cliente = browser.find_element(By.XPATH, '//*[@id="telefone"]')
        telefone_cliente.send_keys(linha['Telefone'])

        cidade_cliente = browser.find_element(By.XPATH, '//*[@id="cidade"]')
        cidade_cliente.send_keys(linha['Cidade'])

        estado_cliente = browser.find_element(By.XPATH, '//*[@id="estado"]')
        estado_cliente.send_keys(linha['Estado'])

        time.sleep(1)

        botao_cadastrar = browser.find_element(By.XPATH, '//*[@id="submit"]')
        botao_cadastrar.click()

        time.sleep(3)

    browser.close()