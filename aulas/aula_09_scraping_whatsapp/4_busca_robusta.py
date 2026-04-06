import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

CONTACT_NAME = "Arduino"

CHROME_PROFILE_PATH = os.path.abspath("chrome_profile")
ELEMENT_TO_WAIT = "//div[@id='pane-side']"
WAIT_TIME = 120 # 2 minutos
SEARCH_BOX_XPATH = "//input[@aria-label='Pesquisar ou começar uma nova conversa']"
SELECT_CONTACT_XPATH = "//span[contains(@class, 'matched-text')]"

VERIFYING_XPATH_PAI = "//*[@id='pane-side']/div/div/div"
VERIFYING_XPATH_INICIAL = "//*[@id='pane-side']/div/div/div/div["
VERIFYING_XPATH_FINAL = "]/div/div/div/div[2]/div[1]/div[1]/div/div/span"
VERIFYING_XPATH_FINAL_GROUP = "]/div/div/div/div[2]/div[1]/div[1]/div/div[1]/span"

def main():
    try:
        manager = ChromeDriverManager().install()
        options = Options()
        options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")
        service = webdriver.chrome.service.Service(manager)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://web.whatsapp.com")

        print("Aguardando elemento do Whatsapp Web ficar visível...")
        wait = WebDriverWait(driver, WAIT_TIME)
        wait.until(EC.presence_of_element_located((
            webdriver.common.by.By.By.XPATH, 
            ELEMENT_TO_WAIT
        )))
        print("Elemento do Whatsapp Web visível!")

        search_box = driver.find_element(webdriver.common.by.By.XPATH, SEARCH_BOX_XPATH)
        search_box.click()
        search_box.send_keys(webdriver.common.keys.Keys.CONTROL + "a")
        search_box.send_keys(webdriver.common.keys.Keys.BACKSPACE)
        time.sleep(0.5)
        for c in CONTACT_NAME:
            search_box.send_keys(c)
            time.sleep(0.1)
        time.sleep(1)

        pai = driver.find_element(webdriver.common.by.By.XPATH, VERIFYING_XPATH_PAI)
        filhos = pai.find_elements(webdriver.common.by.By.XPATH, "./div")
        for i, filho in enumerate(filhos):
            if i == 0:
                continue
            try:
                contact_to_select = driver.find_element(
                    webdriver.common.by.By.XPATH, 
                    VERIFYING_XPATH_INICIAL + str(i+1) + VERIFYING_XPATH_FINAL
                )
            except:
                contact_to_select = driver.find_element(
                    webdriver.common.by.By.XPATH, 
                    VERIFYING_XPATH_INICIAL + str(i+1) + VERIFYING_XPATH_FINAL_GROUP
                )
            print(contact_to_select.text)
            if contact_to_select.text.lower() == CONTACT_NAME.lower():
                print("Contato encontrado!")
                driver.execute_script("arguments[0].scrollIntoView(true);", contact_to_select)
                time.sleep(1)
                contact_to_select.click()
                break
            time.sleep(1)

    except Exception as e:
        print(f"Erro ao raspar o Whatsapp Web: {e}")

    input("Pressione Enter para fechar o driver...")
    driver.quit()

if __name__ == "__main__":
    main()
