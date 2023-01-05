from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()
navegador.get("https://ri.magazineluiza.com.br/")
navegador.find_element(By.XPATH, '//*[@id="Form1"]/div[7]/a').click()
time.sleep(1)
navegador.find_element(By.XPATH, '//*[@id="Form1"]/header/div/div/div/div[1]/button').click()
time.sleep(1)
navegador.find_element(By.XPATH, '//*[@id="heading-mobile-3"]/button').click()
time.sleep(1)
navegador.find_element(By.XPATH, '//*[@id="collapse-mobile-3"]/div/ul/li[2]/a').click()
elemento4 = navegador.find_element(By.XPATH, '//*[@id="D6zgNufoU+5cVlyZe/HZng=="]').click()
time.sleep(0.5)