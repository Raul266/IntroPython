import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager import chrome

chrome = webdriver.Chrome()
chrome.get('https://formy-project.herokuapp.com/form')

'''first_name_field = chrome.find_element(By.ID, 'first-name')
first_name_field.send_keys("Raul")
first_name_field.clear()

last_name_field = chrome.find_element(By.ID, 'last-name')
last_name_field.send_keys("Tudor")

components = chrome.find_element(By.LINK_TEXT, 'Components')
components.click()'''

# enable_and_desable = chrome.find_element(By.PARTIAL_LINK_TEXT,'Enabled')
# enable_and_desable.click()

# drop = chrome.find_elements(By.PARTIAL_LINK_TEXT, 'Drop')[0] # !!! aici indexul incepe de la 0(primul element)
# drop.click()


'''chrome.get('https://www.saucedemo.com/')
username  = chrome.find_element(By.NAME,'user-name')
username.send_keys('Raul')'''

'''input_fields = chrome.find_element(By.TAG_NAME,'input')
input_fields.send_keys('Teodor')

titlu = chrome.find_element(By.TAG_NAME,'h1')
print(titlu.text)

first_name_field = chrome.find_element(By.CLASS_NAME, 'form-control')
first_name_field.clear()
first_name_field.send_keys('Raul')
time.sleep(5)'''

# ! CSS_SELECTOR
# Sintaxa
# se ia numele_tag[nume_atribut = "Val_atributului"],daca vrei sa dai o cautare partiala trebuie pus un * inainte de =
# poti sa cobori mai jos in cautare cu spatiu intre taguri
'''first_name_field = chrome.find_element(By.CSS_SELECTOR, '#first-name') # pt ID se foloseste #
first_name_field.send_keys("Raul")

first_name_field = chrome.find_element(By.CSS_SELECTOR, '.form-control') # pentru class se foloseste .
first_name_field.send_keys("Raul")

first_name_field = chrome.find_element(By.CSS_SELECTOR,"input[placeholder='Enter first name']")'''


# ! XPATH
# Sintaxa
# //numele_tag[@nume_atribut = 'Val_atributului']
first_name = chrome.find_element(By.XPATH,"//input[@id ='first-name']")
first_name.send_keys("RAul")
# pot sa cobor de la un parinte la copil cu / dupa fiecare tag  EX: //form/div/div
# pot sa iau de exemplu al 2 lea input SINTAXA: (//input)[2]
#!!! in XPATH pozitia incepe de la 1 !!!
# se poate cauta cu SAU | exemplu: //noul_TAG | //vechiul_TAG
# alta metoda de cautare daca stim textul pe de pe site(Submit) Ex //nume_tag[text() = "text_de_pe_site"]
time.sleep(5)
