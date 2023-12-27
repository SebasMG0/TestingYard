"""
    @author: Sebatián Murcia for IntegraIT

"""

import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector


URL= "https://euclinicaltrials.eu/app/#/search"


def write(texto):
    with open('html_ejemplo.html', 'w', encoding='utf-8')  as f:
        f.write(texto)

def configDriver():
    options = Options()
    # options.add_argument('-headless') # Configuración para que no se abra el navegador
    driver=webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    return driver

def searchResults(driver):
    driver.get(URL)
    
    driver.execute_script("arguments[0].click()",
                          driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]"))

    driver.execute_script("arguments[0].remove();", 
                         driver.find_element(By.XPATH, "//div[@class='ngx-spinner-overlay ng-tns-c11-0 ng-trigger ng-trigger-fadeIn ng-star-inserted ng-animating']"))

    WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//td")))
    counter=0
    while counter<10:
        writeLinksSQL([(row.find('a').get('href'), False) for row in BeautifulSoup(driver.page_source, 'lxml').find_all("tr")[1:]])
        try: driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")); time.sleep(0.1)
        except: print('\n-- Finalizado --\n'); return
        counter+=1
    
    
def writeLinksTXT(link):
    with open("links.txt", 'a', encoding='utf-8'):
        write(link+"\n")

def connect():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="RootUser.23",
    database="EUDRA"
    )

def writeLinksSQL(values:list):
    cnx= connect()
    SQL = "INSERT into links  (path, extracted) VALUES (%s, %s)"
    cursor = cnx.cursor()
    for i in values:
        try:
            cursor.execute(SQL, i)
            cnx.commit()
        except:
            continue

    cursor.close()
    cnx.close()

def getLinks():
    cnx=connect()
    cursor= cnx.cursor()
    SQL= 'select path from links where extracted=false'
    try:
        return cursor.execute(SQL)
    except:
        print("Error en la obtención de los links")
        raise
    finally:
        cnx.close()
        cursor.close()

def extract_info():
    BASE_URL= "https://euclinicaltrials.eu/app/"
    driver= configDriver()
    # links= getLinks()
    # for i in links:
    link= BASE_URL+ "#/view/2022-500024-30-00"

    driver.get(link)
    WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Full trial information')]")))
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//div[contains(text(), 'Full trial information')]"))
    WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Trial details')]")))
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//span[contains(text(), 'Trial details')]"))
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//span[contains(text(), 'Sponsors')]"))
    
    
    # sponsors= driver.find_elements(By.XPATH, "//input[@id='sponsor.id']")
    sponsors= driver.find_elements(By.XPATH, "//table")
    print(BeautifulSoup(sponsors[0]))
        
        

# searchResults(configDriver())
extract_info()


    



