from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome = webdriver.Chrome()

class LoginTests(unittest.TestCase):
    def login(self,user,password):
        chrome.find_element(By.ID, "user-name").send_keys(user)
        chrome.find_element(By.NAME, "password").send_keys(password)
        chrome.find_element(By.ID, "login-button").click()

    def setUp(self):
        chrome.get("https://www.saucedemo.com/")
    def test_login_incorect(self):
        self.login('alabala','alabala')

        # actual = chrome.find_element(By.XPATH, "//h3[@data-test='error']").text
        # expected = "Epic sadface: Username and password do not match any user in this service']"
        # assert actual == expected, "Mesajul de eroare nu e corect"

        actual = chrome.current_url
        expected= "https://www.saucedemo.com/"
        self.assertEqual(expected,actual, "Am reusit sa ma loghez cu credentialele incorecte")
        sleep(4)

    def test_login_corect(self):
        self.login("standard_user","secret_sauce")

        actual = chrome.current_url
        expected = "https://www.saucedemo.com/inventory.html"
        self.assertEqual(expected,actual,"Nu suntem pe pagina la care ne asteptam")

    def test_login_user_blocat(self):
        self.login('locked_out_user','secret_sauce')

        # actual = chrome.find_element(By.XPATH,"//h3[@data-test = 'error']").text
        # expected = 'Epic sadface: Sorry, this user has been locked out.'
        # assert actual == expected , 'Mesajul de eroare este diferit'

        actual = chrome.find_element(By.XPATH, "//h3[@data-test = 'error']").text
        expected = 'Epic sadface: Sorry, this user has been locked out.'
        self.assertEqual(expected,actual,'Mesajul de eroare este diferit')

    def test_login_parola_lipsa(self):
        self.login("standard_user","")
        actual = chrome.find_element(By.TAG_NAME,'h3').text
        expected  = 'Epic sadface: Password is required'
        self.assertEqual(actual,expected,'Mesajul de lipsa parola este diferit')

