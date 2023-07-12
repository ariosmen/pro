from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import os

if not os.path.exists('download'):
    os.mkdir('download')

URL = "https://datos.gob.es/"
PATH = os.path.join(os.getcwd(), "download")
TIME_OUT = 10
FILE_DOWNLOAD = "padron.csv"
DIR_DOWNLOAD = os.path.join(PATH, FILE_DOWNLOAD)

def download():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"download.default_directory": PATH})
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(URL)

    call = WebDriverWait(driver, TIME_OUT).until(
        EC.presence_of_element_located(
            (By.XPATH, "//ul[@class='menu']//li/a[@href='#data']")
        )
    )

    call.click()

    call = WebDriverWait(driver, TIME_OUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//li[@class='expanded menu-mlid-865 is-visible']//li/a[@href='/es/catalogo']",
            )
        )
    )
    call.click()

    call = WebDriverWait(driver, TIME_OUT).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='search_bar']"))
    )
    call.send_keys("Padron ciego", Keys.ENTER)

    call = WebDriverWait(driver, TIME_OUT).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class='label csv']"))
    )
    call.click()

    call = driver.find_element(
        By.XPATH, "//a[@href='https://opendata-santboi.hub.arcgis.com/datasets/santboi::padró-dhabitants.csv?outSR=%7B%22latestWkid%22%3A25831%2C%22wkid%22%3A25831%7D']"
    ).get_attribute("href")
    driver.quit()
    response = requests.get(call)
    
    with open(f"{DIR_DOWNLOAD}", 'wb') as file:
        file.write(response.content)

    # from urllib import request
    
    # call = driver.find_element(
    #     By.XPATH, "//a[@href='https://opendata-santboi.hub.arcgis.com/datasets/santboi::padró-dhabitants.csv?outSR=%7B%22latestWkid%22%3A25831%2C%22wkid%22%3A25831%7D']"
    # ).get_attribute("href")
    # local_file = f"{DIR_DOWNLOAD}"
    # request.urlretrieve(call, local_file)
