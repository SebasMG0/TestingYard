import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


URL= "https://sisa.msal.gov.ar/sisa/#sisa"

# Manejadores de índices externos
global_win_index= 1
global_tab_index= 1

def driver_default_wait(driver):
    # Espera por defecto para que se cargue
    WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.TAG_NAME, "table")))
    time.sleep(2.25)

def config_driver():
    # Inicialización del driver
    options= Options()
    # options.add_argument('-headless') # Configuración para que no se abra el navegador
    driver = webdriver.Chrome(options=options)
    return driver

def goto_table(driver):
    # Clic en el botón Renis
    driver.find_elements(By.XPATH, "//div[@class='col-xs-3']/a")[5].click()
    driver_default_wait(driver)

    # Clic en el botón Consultar Información Registrada
    driver.execute_script("arguments[0].click()", driver.find_element(By.XPATH, '//*[@id="divSISA"]/div/div[1]/div[3]/div[2]/div/table/tbody/tr/td[4]/table/tbody/tr[6]/td/table/tbody/tr[1]/td[2]/div/img'))
    driver_default_wait(driver)

    # Clic en el botón Centros de investigación
    driver.execute_script("arguments[0].click()", driver.find_element(By.XPATH, '//*[@id="s_consultar_info_renis"]/table/tbody/tr[3]/td/table/tbody/tr[1]/td[4]/div/img'))
    driver_default_wait(driver)

    # Cambiar a la página de la extracción
    input_element= driver.find_element(By.XPATH, "/html/body/div[3]/table/tbody/tr[2]/td/div/div/div[1]/div[3]/div[2]/div/table/tbody/tr/td[4]/table/tbody/tr[8]/td/div/div/div[3]/table/tbody/tr[4]/td/table/tbody/tr[4]/td/div/table/tbody/tr[2]/td/div/div/div[3]/table/tbody/tr[7]/td/div/div/div/div[4]/div/div[9]/div/div[3]/input")
    driver_default_wait(driver)
    input_element.clear()
    input_element.send_keys(global_win_index-1)
    
    driver.find_element(By.XPATH, "/html/body/div[3]/table/tbody/tr[2]/td/div/div/div[1]/div[3]/div[2]/div/table/tbody/tr/td[4]/table/tbody/tr[8]/td/div/div/div[3]/table/tbody/tr[4]/td/table/tbody/tr[4]/td/div/table/tbody/tr[2]/td/div/div/div[3]/table/tbody/tr[7]/td/div/div/div/div[4]/div/div[9]/div/div[4]/a").click()
    driver_default_wait(driver)


def extract(url, csv_writer):
    # Variables de control externas
    global global_tab_index
    global global_win_index

    # Acceder a la página
    driver= config_driver()
    driver.get(url)
    driver_default_wait(driver)

    # Acceso a la tabla para extraer la información e índices actuales 
    goto_table(driver)
    max_win_index= driver.find_element(By.XPATH, "/html/body/div[3]/table/tbody/tr[2]/td/div/div/div[1]/div[3]/div[2]/div/table/tbody/tr/td[4]/table/tbody/tr[8]/td/div/div/div[3]/table/tbody/tr[4]/td/table/tbody/tr[4]/td/div/table/tbody/tr[2]/td/div/div/div[3]/table/tbody/tr[7]/td/div/div/div/div[4]/div/div[10]/div/div[2]").text.split(" ")
    driver_default_wait(driver)

    # Ciclo de acceso y extracción por página
    while global_win_index <= int(max_win_index[4]): # and global_win_index <= 40:
        rows= driver.find_elements(By.XPATH, '//*[@id="s_consultar_info_renis_lista_283_3"]/table/tbody/tr[2]/td/div/div/div[3]/table/tbody/tr[8]/td/div/div/div/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr')
        driver_default_wait(driver)

        while global_tab_index < len(rows):
            # Clic en la imagen que muestra el detalle del registro
            driver.execute_script("arguments[0].click()", rows[global_tab_index].find_element(By.XPATH, "td[8]/div/img"))
            driver_default_wait(driver)

            # Extracción de la información en el detalle del sitio
            extract_detail(driver, csv_writer)
            driver_default_wait(driver)
            global_tab_index+=1
            
            # Acceso a la tabla de sitios nuevamente
            goto_table(driver)

            # Nueva búsqueda de filas
            rows= driver.find_elements(By.XPATH, '//*[@id="s_consultar_info_renis_lista_283_3"]/table/tbody/tr[2]/td/div/div/div[3]/table/tbody/tr[8]/td/div/div/div/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr')

        # Actualización de índices
        global_tab_index= 1
        global_win_index+= 1

        # Clic en el botón de siguiente página
        driver.find_element(By.XPATH, "/html/body/div[3]/table/tbody/tr[2]/td/div/div/div[1]/div[3]/div[2]/div/table/tbody/tr/td[4]/table/tbody/tr[8]/td/div/div/div[3]/table/tbody/tr[4]/td/table/tbody/tr[4]/td/div/table/tbody/tr[2]/td/div/div/div[3]/table/tbody/tr[7]/td/div/div/div/div[4]/div/div[9]/div/div[4]/a").click()
        driver_default_wait(driver)
        
        

def extract_detail(driver, csv_writer):
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extracción de los elementos con datos
    data= soup.find_all('div', class_= "gwt-HTML", text=True)

    #  Escribe en el csv los campos extraídos
    try:
        csv_writer.writerow(
            [data[1].text,
            data[2].text,
            data[4].text,
            data[5].text,
            data[6].text,
            data[7].text,
            data[-1].text,
            data[-2].text]
            )
    except:
        pass

    # Cierra el detalle del registro
    driver.execute_script("arguments[0].click()", driver.find_element(By.XPATH, "//a"))
    driver_default_wait(driver)


def exe(fields:list, csv_file:str, header:bool):
    with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file:
        if header: csv.DictWriter(csv_file, fieldnames=fields).writeheader()
        csv_writer= csv.writer(csv_file)

        try:
            extract(URL, csv_writer)

        except:

            print("-----------Finalizado-----------")
            print(f"Win de fallo: {global_win_index} Tab de fallo: {global_tab_index}")
            with open("file.txt" , 'w') as file:
                file.write(f"Win de fallo: {global_win_index} Tab de fallo: {global_tab_index}")
            raise


# Campos para el header del csv
fields=[
        "codigo",
        "tipo_institucion",
        "nombre_institucion",
        "nombre_autoridad",
        "pagina_web",
        "fuente_financiacion",
        "correo",
        "responsable registro"
    ]

exe(fields, 'sisa4311__v1.csv', True)

# Función para combinar todos archivos de tipo csv si se divide la extracción
import os
import csv

def get_csv_titles(directory):
    titles = []
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            titles.append(filename)
    titles.sort()
    return titles

def merge_csv(fields, merged_file_name, csvs:list):
    with open(merged_file_name, 'w', encoding='utf-8', newline='') as merged_file:
        writer= csv.writer(merged_file)
        writer.writerow(fields)
        for i in csvs:
            with open(i, 'r', encoding='utf-8') as file:
                reader= csv.reader(file)
                line= next(reader)
                while(len(line)>0):
                    writer.writerow(line)
                    try:
                        line= next(reader)
                    except :
                        break

# merge_csv(fields, 'merged_sisa_v1', get_csv_titles("D:\Biblioteca Win\Escritorio\IntegraIt\ClinicalTrialsWebScraper\SISA"))
