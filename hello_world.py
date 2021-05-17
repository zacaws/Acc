from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
import random

#localização do chromedriver.exe
PATH = "C:/Users/diego/Desktop/Programação/Account Creator/chromedriver.exe"
driver = webdriver.Chrome(PATH)

#abrir website
driver.get("https://habbo.com.br")
print(driver.title)


try:
	#rejeita cookies
	element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, "onetrust-reject-all-handler"))
		)
	element.click()

	time.sleep(5)

	#Localiza e clica no Entre Agora
	element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.LINK_TEXT, "ENTRE AGORA!"))
		)
	element.click()
	time.sleep(4)


	#EMAIL
#!!!ARRUMAR COM UMA TABELA DINÂMICA DO EXCEL
	element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, "email-address"))
		)
	element.click()
	element.clear()
	time.sleep(1)
	#Escreve os emails
#!!!ARRUMAR COM UMA TABELA DINÂMICA DO EXCEL
	element.send_keys("EXCEL EMAILS")

	time.sleep(3)

	#SENHA
	element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, "password-new"))
		)
	element.click()
	element.clear()
	time.sleep(1)
	#Escreve as senhas
#!!!ARRUMAR COM UMA TABELA DINÂMICA DO EXCEL
	element.send_keys("senhasmuitosecretas123")


	#REPETIR SENHA
	element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, "password-new-repeated"))
		)
	element.click()
	element.clear()
	#Escreve as senhas
#!!!ARRUMAR COM UMA TABELA DINÂMICA DO EXCEL
	element.send_keys("senhasmuitosecretas123")


	#DATA DE NASCIMENTO

	#Mes
	monthrand = random.randint(1, 12)
	print(monthrand)
	select = Select(driver.find_element_by_xpath("//select[@ng-model='BirthdateController.month']"))
	#seleciona atraves de uma STRING
	select.select_by_value(str(monthrand))
	print(select)

	time.sleep(2)

	#Ano
	yearrand = random.randint(1997, 2005)
	print(yearrand)
	select = Select(driver.find_element_by_xpath("//select[@ng-model='BirthdateController.year']"))
	#seleciona atraves de uma STRING
	select.select_by_value(str(yearrand))
	print(select)

	time.sleep(2)

	#Dia
	dayrand = random.randint(1, 27)
	print(dayrand)
	select = Select(driver.find_element_by_xpath("//select[@ng-model='BirthdateController.day']"))
	#seleciona atraves de uma STRING
	select.select_by_value(str(dayrand))
	print(select)

	time.sleep(2)


	#CheckBoxes
	element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, "terms-of-service"))
		)
	element.click()

	time.sleep(2)

	#reCaptcha
	element = WebDriverWait(driver, 10).until(
			EC.text_to_be_present_in_element_value(By.XPATH, "//div[@id='recaptcha-accessible-status']")
		)
	
	print(element)



finally:
	driver.quit()


#alerta que o programa vai rodar

#Abrir area de trabalho
#clicar na lupa
#digitar Edge
#abrir o Edge
#esperar X segundos
#digitar habbo
#clicar no "entre agora"
#clicar no campo e-mail
#digitar email de uma tabela do excel
#digitar senha
#confirmar senha
#selecionar data de nascimento
#dia
#mes
#ano
#aceitar termos
#alerta para completar o código captcha
#após completar clicar no OK
#clicar no feito crie seu avatar