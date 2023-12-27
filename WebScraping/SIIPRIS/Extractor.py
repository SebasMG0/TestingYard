# -*- coding: utf-8 -*-
"""
    Author: Sebastián Murcia for IntegraIT
    Date created: 05/07/2023
    Description: Code to extract information published by COFEPRIS on SIIPRIS (Mexico).
                It should be noted that the contact information and email are combined
                in a single field and it is necessary to use external tools for their
                respective adjustment. At the time of writing the code, Perplexity AI and MySQL were used.
"""

import re
import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL= "http://siipris03.cofepris.gob.mx/Resoluciones/Consultas/ConWebRegEnsayosClinicos.asp"


def configDriver():
    options = Options()
    #options.add_argument('-headless') # Configuración para que no se abra el navegador
    driver = webdriver.Firefox(options=options)
    return driver

def getInfo(driver:webdriver, csv_writer)->None:
        #WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "txt_gral")))
        time.sleep(0.1)
        soup= BeautifulSoup(driver.page_source, features='html.parser', from_encoding='utf-8')
        table = soup.find_all('table', {'class': 'txt_gral'})[-1]
        rows= table.find_all('tr', {'class': 'txt_gral'})

        for row in rows:
            try:
                cols= row.find_all('td')
                onclick = re.search(r'onclick="([^"]*)"', str(cols[2])).group(1)
                number = re.search(r'SelFicha\((\d+)\)', onclick).group(1)
                link= driver.find_element(by=By.XPATH, value=f"//a[contains(@onclick, '{number}')]")
                link.click()
                data= getInfoFromPopUp(driver)

                if data[6]=='NR': raise TypeError

                name, email= data[6].strip().replace("\n","").replace("\t"," ").rsplit(" ", 1)
                if email.find("@")==-1: continue
                csv_writer.writerow(formatInfo([data[0], data[2], data[4], data[5], name, email, data[7], data[10],data[11], data[12], data[13],
                        data[20]]))
            except:
                continue


def getInfoFromPopUp(driver):
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 2.5).until(EC.presence_of_element_located((By.CLASS_NAME, "txt_gral")))
    rows= BeautifulSoup(driver.page_source).find_all('tr')

    if len(rows)<10: return

    data= []
    for row in rows[1:]:
        try:
            data.append(row.find("td").text)
        except:
            data.append("NR")

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return data


def getResultPage(driver, url):
    driver.get(url)
    btn_search = driver.find_element(by=By.XPATH, value="//input[@id='button' and @class='txt_gral']")
    btn_search.click()


def formatInfo(fields:list)-> list:
    for i in range (len(fields)):
        fields[i]=fields[i].strip().replace("\n", " ").replace("\t", " ")
    return fields

def exe(fields:list, csv_file:str)->None:
    driver= configDriver()
    getResultPage(driver, URL)

    with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file:
        csv.DictWriter(csv_file, fieldnames=fields).writeheader()
        csv_writer= csv.writer(csv_file)

        try:
            while True:
                getInfo(driver, csv_writer)
                nextButton= driver.find_element(By.XPATH, "//a[text()='Siguiente']")
                nextButton.click()


        except:
            print("-----------Finalizado-----------")

if __name__=="__main__":
    fields= [
        "Número de ingreso",
        "Número de protocolo",
        "Patrocinador",
        "Proveedor de información",
        "Nombre",
        "Email",
        "Título público",
        "Países de reclutamiento potencial",
        "Sitio de investigación",
        "Condición",
        "Área terapeutica",
        "Tipo de estudio"
    ]
    exe(fields=fields, csv_file="saved_siipris_data.csv")
